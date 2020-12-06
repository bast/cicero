import io
import os
import flask
from .images import fix_images
from .render import render

blueprint = flask.Blueprint("preview", __name__)


@blueprint.route("/")
def home():
    config = flask.current_app.config

    md_file_prefix, _ = os.path.splitext(config["filename"])

    try:
        with io.open(config["filename"], "r", encoding="utf-8") as f:
            markdown = f.read()
    except UnicodeDecodeError:
        with io.open(config["filename"], "r", encoding="cp1252") as f:
            markdown = f.read()
    markdown = fix_images(markdown, "images/")

    return render(
        engine=config["engine"],
        url_prefix=None,
        md_file_prefix=md_file_prefix,
        markdown=markdown,
    )


@blueprint.route("/images/<path:path>")
def serve_image(path):
    config = flask.current_app.config
    return flask.send_from_directory(config["imagedir"], path)


@blueprint.errorhandler(404)
def page_not_found(e):
    return flask.render_template("404.html"), 404
