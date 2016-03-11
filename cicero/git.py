import flask

blueprint = flask.Blueprint('git', __name__)


@blueprint.route('/')
def home():
    return flask.render_template('index.html')


@blueprint.route('/v1/github/<user_name>/<repo_name>/<branch_name>/<file_name>/remark/')
def talk(user_name, repo_name, branch_name, file_name):
    from urllib import request
    from .images import fix_images

    try:
        url = 'https://raw.githubusercontent.com/{}/{}/{}/{}'.format(user_name, repo_name, branch_name, file_name)

        response = request.urlopen(url)

        markdown = response.readlines()
        markdown = [line.decode("utf-8") for line in markdown]
        if markdown == 'Not Found':
            return flask.render_template('404.html')

            # we do not use https://raw.githubusercontent.com because it does not handle svg files
        prefix = 'https://cdn.rawgit.com/{}/{}/{}/'.format(user_name, repo_name, branch_name)
        return flask.render_template('slides.html', markdown=''.join(fix_images(markdown, prefix)))
    except IOError:
        return flask.render_template('404.html')
