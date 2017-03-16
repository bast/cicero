import os
import flask
import sys

if sys.version_info[0] > 2:
    from urllib import request
    _urlopen = request.urlopen
else:
    import urllib2
    _urlopen = urllib2.urlopen

blueprint = flask.Blueprint('git', __name__)

URL_BASE = 'CICERO_URL_BASE_is_undefined'
_url_base = os.environ.get('CICERO_URL_BASE')
if _url_base is not None:
    URL_BASE = _url_base


def set_url_base(host, port):
    global URL_BASE
    URL_BASE = 'http://{}:{}'.format(host, port)


@blueprint.route('/')
def home():
    return flask.render_template('index.html', url_base=URL_BASE)


def render_github_markdown(path):
    from .title import extract_title
    from .images import fix_images

    try:
        url = 'https://raw.githubusercontent.com/{}'.format(path)

        response = _urlopen(url)

        markdown = response.read().decode("utf-8")
        if markdown == 'Not Found':
            return flask.render_template('404.html')

        # we do not use https://raw.githubusercontent.com because it does not handle svg files

        # we define root as everything except the last file
        root = '/'.join(path.split('/')[:-1])
        prefix = 'https://cdn.rawgit.com/{}/'.format(root)

        title = extract_title(markdown)
        style = flask.request.args.get('style')
        if style is None:
            style = 'default'

        try:
            url = 'https://raw.githubusercontent.com/{}/{}'.format(root, 'remark.html')
            response = _urlopen(url)
            template = response.read().decode("utf-8")
            return flask.render_template_string(template,
                                                title=title,
                                                markdown=fix_images(markdown, prefix),
                                                style=style)
        except IOError:
            return flask.render_template('remark.html',
                                         title=title,
                                         markdown=fix_images(markdown, prefix),
                                         style=style)
    except IOError:
        return flask.render_template('404.html')


@blueprint.route('/v1/github/<path:path>/remark/')
def render_v1(path):
    return render_github_markdown(path)


@blueprint.route('/v2/remark/github/<path:path>/')
def render_v2(path):
    return render_github_markdown(path)
