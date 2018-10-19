import os
import flask
import sys
import requests
import json

blueprint = flask.Blueprint('git', __name__)

URL_BASE = 'CICERO_URL_BASE_is_undefined'
_url_base = os.environ.get('CICERO_URL_BASE')
if _url_base is not None:
    URL_BASE = _url_base


def get_sha_github(owner, repo, ref):
    uri = 'https://api.github.com/repos/{0}/{1}/commits/{2}'.format(owner, repo, ref)
    response = requests.get(uri)
    data = json.loads(response.text)
    return data['sha']


def test_get_sha_github():
    is_travis_build = os.getenv('TRAVIS', False)
    # Travis CI is rate-limited by GitHub API
    if not is_travis_build:
        sha = get_sha_github('bast', 'cicero', 'bfa3748447')
        assert sha == 'bfa3748447fe0c7455f19a027575406a0c561a4f'


def set_url_base(host, port):
    global URL_BASE
    URL_BASE = 'http://{}:{}'.format(host, port)


@blueprint.route('/')
def home():
    return flask.render_template('index.html', url_base=URL_BASE)


def render_url_markdown(path, engine, engine_version):
    from .title import extract_title
    from .images import fix_images

    service, owner, repo, ref, *_md_file_path = path.split('/')
    md_file_path = '/'.join(_md_file_path)
    md_file_path_root = '/'.join(_md_file_path[:-1])
    md_file = _md_file_path[-1]

    if service == 'github.com':
        # we need to translate the reference to a sha (the reference can be a sha)
        # the reason for this is that cdn.rawgit.com caches files forever
        # the reference may change but the sha won't
        # when changing to https://www.jsdelivr.com i haven't verified whether
        # results are cached so translating to hashes might be overkill
        sha = get_sha_github(owner, repo, ref)

        root = '{0}/{1}@{2}'.format(owner, repo, sha)

        url_prefix = 'https://cdn.jsdelivr.net/gh/{0}/'.format(root)
    elif service == 'gitlab.com':
        url_prefix = 'https://{0}/{1}/{2}/raw/{3}/'.format(service, owner, repo, ref)
    else:
        *_url_prefix, md_file = path.split('/')
        url_prefix = 'https://' + '/'.join(_url_prefix)
        md_file_path = md_file
        md_file_path_root = ''

    md_file_prefix, _ = os.path.splitext(md_file)

    if '/' in md_file_path:
        url_prefix += md_file_path_root

    url = url_prefix + '/' + md_file

    response = requests.get(url)
    if response.status_code == 404:
        return flask.render_template('404.html')

    markdown = response.text

    title = extract_title(markdown)
    style = flask.request.args.get('style')
    if style is None:
        style = 'default'

    # if own css is available, we load it
    # if not, we default to empty own css
    url = url_prefix + '/' + md_file_prefix + '.css'
    response = requests.get(url)
    if response.status_code == 404:
        own_css = ''
    else:
        own_css = response.text
        own_css = flask.Markup(own_css)  # disable autoescaping

    # .. do the same for own javascript
#   url = url_prefix + '/' + md_file_prefix + '.js'
#   response = requests.get(url)
#   if response.status_code == 404:
#       own_javascript = ''
#   else:
#       own_javascript = response.text
    # for the moment I am not sure whether the above is not too risky
    own_javascript = ''

    # use custom configuration for the rendering engine, if available
    url = url_prefix + '/' + md_file_prefix + '.conf'
    response = requests.get(url)
    if response.status_code == 404:
        own_conf = ''
    else:
        own_conf = ',\n'.join(response.text.split('\n'))

    return flask.render_template('render.html',
                                 title=title,
                                 markdown=fix_images(markdown, url_prefix),
                                 style=style,
                                 own_css=own_css,
                                 own_javascript=own_javascript,
                                 own_conf=own_conf,
                                 engine='{0}-{1}'.format(engine, engine_version))


@blueprint.route('/v1/github/<path:path>/remark/')
def render_v1(path):
    return render_url_markdown('github.com' + '/' + path, 'remark', '0.13.0')


@blueprint.route('/v2/remark/github/<path:path>/')
def render_v2(path):
    return render_url_markdown('github.com' + '/' + path, 'remark', '0.13.0')


@blueprint.route('/v3/<string:engine>/<string:engine_version>/<path:path>/')
def render_v3(path, engine, engine_version):
    return render_url_markdown(path, engine, engine_version)
