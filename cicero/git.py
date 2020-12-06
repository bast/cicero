import io
import os
import flask
import sys
import requests
import json
from .version import __version__
from .images import fix_images
from .render import render

blueprint = flask.Blueprint("git", __name__)

URL_BASE = "CICERO_URL_BASE_is_undefined"
_url_base = os.environ.get("CICERO_URL_BASE")
if _url_base is not None:
    URL_BASE = _url_base


def get_sha_github(owner, repo, ref):
    uri = "https://api.github.com/repos/{0}/{1}/commits/{2}".format(owner, repo, ref)
    response = requests.get(uri)
    data = json.loads(response.text)
    return data["sha"]


def test_get_sha_github():
    sha = get_sha_github("bast", "cicero", "bfa3748447")
    assert sha == "bfa3748447fe0c7455f19a027575406a0c561a4f"


def set_url_base(host, port):
    global URL_BASE
    URL_BASE = "http://{}:{}".format(host, port)


@blueprint.route("/")
def home():
    return flask.render_template("index.html", url_base=URL_BASE, version=__version__)


def render_url_markdown(path, engine, engine_version):

    service, owner, repo, ref, *_md_file_path = path.split("/")
    md_file_path = "/".join(_md_file_path)
    md_file_path_root = "/".join(_md_file_path[:-1])
    md_file = _md_file_path[-1]

    if service == "github.com":
        # in the old days we used cdn.rawgit.com which cached files forever
        # and therefore instead of referencing the branch, we referenced the sha
        # not sure whether raw.githubusercontent.com caches files
        # so translating to hashes might be overkill
        sha = get_sha_github(owner, repo, ref)
        url_prefix = "https://raw.githubusercontent.com/{0}/{1}/{2}/".format(
            owner, repo, sha
        )
        # we use this image_url_prefix workaround since
        # raw.githubusercontent.com does not render svg
        image_url_prefix = "https://cdn.jsdelivr.net/gh/{0}/{1}@{2}".format(
            owner, repo, sha
        )
    elif service == "gitlab.com":
        url_prefix = "https://{0}/{1}/{2}/raw/{3}/".format(service, owner, repo, ref)
        image_url_prefix = url_prefix
    else:
        *_url_prefix, md_file = path.split("/")
        url_prefix = "https://" + "/".join(_url_prefix)
        image_url_prefix = url_prefix
        md_file_path = md_file
        md_file_path_root = ""

    md_file_prefix, _ = os.path.splitext(md_file)

    if "/" in md_file_path:
        url_prefix += md_file_path_root

    url = url_prefix + "/" + md_file
    response = requests.get(url)
    if response.status_code == 404:
        return flask.render_template("404.html")
    markdown = response.text

    markdown = fix_images(markdown, image_url_prefix + "/")

    return render(
        engine="{0}-{1}".format(engine, engine_version),
        url_prefix=url_prefix,
        md_file_prefix=md_file_prefix,
        markdown=markdown,
    )


@blueprint.route("/v1/github/<path:path>/remark/")
def render_v1(path):
    return render_url_markdown("github.com" + "/" + path, "remark", "legacy")


@blueprint.route("/v2/remark/github/<path:path>/")
def render_v2(path):
    return render_url_markdown("github.com" + "/" + path, "remark", "legacy")


@blueprint.route("/v3/<string:engine>/<string:engine_version>/<path:path>/")
def render_v3(path, engine, engine_version):
    return render_url_markdown(path, engine, engine_version)
