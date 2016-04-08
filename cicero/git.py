import flask

blueprint = flask.Blueprint('git', __name__)


@blueprint.route('/')
def home():
    return flask.render_template('index.html')


def render_github_markdown(namespace, repo, branch, file_name):
    from urllib import request
    from .images import fix_images

    try:
        url = 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(namespace, repo, branch, file_name)

        response = request.urlopen(url)

        markdown = response.readlines()
        markdown = [line.decode("utf-8") for line in markdown]
        if markdown == 'Not Found':
            return flask.render_template('404.html')

        # we do not use https://raw.githubusercontent.com because it does not handle svg files
        if '/' in file_name:
            # we define root as everything except the last file
            root = '/'.join(file_name.split('/')[:-1])
            prefix = 'https://cdn.rawgit.com/{}/{}/{}/{}/'.format(namespace, repo, branch, root)
        else:
            prefix = 'https://cdn.rawgit.com/{}/{}/{}/'.format(namespace, repo, branch)

        return flask.render_template('slides.html', markdown=fix_images(markdown, prefix))
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
