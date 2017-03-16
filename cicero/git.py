import os
import flask
import sys

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


def render_github_markdown(namespace, repo, branch, file_name):
    from .title import extract_title
    from .images import fix_images

    if sys.version_info[0] > 2:
        from urllib import request
    else:
        import urllib2

    try:
        url = 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(namespace, repo, branch, file_name)

        if sys.version_info[0] > 2:
            response = request.urlopen(url)
        else:
            response = urllib2.urlopen(url)

        markdown = response.read().decode("utf-8")
        if markdown == 'Not Found':
            return flask.render_template('404.html')

        # we do not use https://raw.githubusercontent.com because it does not handle svg files
        if '/' in file_name:
            # we define root as everything except the last file
            root = '/'.join(file_name.split('/')[:-1])
            prefix = 'https://cdn.rawgit.com/{}/{}/{}/{}/'.format(namespace, repo, branch, root)
        else:
            prefix = 'https://cdn.rawgit.com/{}/{}/{}/'.format(namespace, repo, branch)

        title = extract_title(markdown)
        style = flask.request.args.get('style')
        if style is None:
            style = 'default'

        try:
            url = 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(namespace, repo, branch, 'remark.html')
            if sys.version_info[0] > 2:
                response = request.urlopen(url)
            else:
                response = urllib2.urlopen(url)
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


@blueprint.route('/v1/github/<namespace>/<repo>/<branch>/<f1>/remark/')
def render_v1(namespace, repo, branch, f1):
    return render_github_markdown(namespace, repo, branch, f1)


# ugly solution, should go with regex but is convoluted with blueprints

@blueprint.route('/v2/remark/github/<namespace>/<repo>/<branch>/<f1>/')
def render_v2_1(namespace, repo, branch, f1):
    return render_github_markdown(namespace, repo, branch, f1)


@blueprint.route('/v2/remark/github/<namespace>/<repo>/<branch>/<f1>/<f2>/')
def render_v2_2(namespace, repo, branch, f1, f2):
    return render_github_markdown(namespace, repo, branch, '/'.join([f1, f2]))


@blueprint.route('/v2/remark/github/<namespace>/<repo>/<branch>/<f1>/<f2>/<f3>/')
def render_v2_3(namespace, repo, branch, f1, f2, f3):
    return render_github_markdown(namespace, repo, branch, '/'.join([f1, f2, f3]))


@blueprint.route('/v2/remark/github/<namespace>/<repo>/<branch>/<f1>/<f2>/<f3>/<f4>/')
def render_v2_4(namespace, repo, branch, f1, f2, f3, f4):
    return render_github_markdown(namespace, repo, branch, '/'.join([f1, f2, f3, f4]))


@blueprint.route('/v2/remark/github/<namespace>/<repo>/<branch>/<f1>/<f2>/<f3>/<f4>/<f5>/')
def render_v2_5(namespace, repo, branch, f1, f2, f3, f4, f5):
    return render_github_markdown(namespace, repo, branch, '/'.join([f1, f2, f3, f4, f5]))
