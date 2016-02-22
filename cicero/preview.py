import io
import flask
from .images import fix_images

blueprint = flask.Blueprint('preview', __name__)


@blueprint.route('/')
def home():
    config = flask.current_app.config

    with io.open(config['filename'], 'r', encoding='utf-8') as mkdfile:
        markdown = mkdfile.readlines()

    markdown = ''.join(fix_images(markdown, 'images/'))

    return flask.render_template('slides.html', markdown=markdown)


@blueprint.route('/images/<path:path>')
def serve_image(path):
    config = flask.current_app.config
    return flask.send_from_directory(config['imagedir'], path)


@blueprint.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
