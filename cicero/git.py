import flask
import urllib

import paths
from .images import fix_images

app = flask.Flask('Cicero',
                  template_folder=paths.TEMPLATE_FOLDER,
                  static_folder=paths.STATIC_FOLDER)


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/v1/github/<user_name>/<repo_name>/<branch_name>/<file_name>/remark/')
def talk(user_name, repo_name, branch_name, file_name):
    try:
        f = urllib.urlopen("https://raw.githubusercontent.com/%s/%s/%s/%s" % (user_name, repo_name, branch_name, file_name))
        markdown = f.readlines()
        if markdown == "Not Found":
            return flask.render_template('404.html')
        # we do not use https://raw.githubusercontent.com because it does not handle svg files
        prefix = "https://cdn.rawgit.com/%s/%s/%s/" % (user_name, repo_name, branch_name)
        return flask.render_template('slides.html', markdown=''.join(fix_images(markdown, prefix)))
    except IOError:
        return flask.render_template('404.html')


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
