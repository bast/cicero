import io
import os
import flask
from .title import extract_title
from .images import fix_images
from jinja2 import Template

blueprint = flask.Blueprint('preview', __name__)


def _read_if_exists(custom_prefix, suffix, engine):
    custom_file_name = custom_prefix + '.' + suffix
    vendor_file_name = os.path.join(os.path.dirname(__file__), 'templates', 'engines', engine, 'vendor.' + suffix)
    for file_name in [custom_file_name, vendor_file_name]:
        if os.path.isfile(file_name):
            with io.open(file_name, 'r') as f:
                # disable autoescaping
                return f.read()
    return ''


@blueprint.route('/')
def home():

    config = flask.current_app.config

    try:
        with io.open(config['filename'], 'r', encoding='utf-8') as mkdfile:
            markdown = mkdfile.read()
    except UnicodeDecodeError:
        with io.open(config['filename'], 'r', encoding='cp1252') as mkdfile:
            markdown = mkdfile.read()

    title = extract_title(markdown)
    markdown = fix_images(markdown, 'images/')

    style = flask.request.args.get('style')
    if style is None:
        style = 'default'

    talk_no_suffix, _suffix = os.path.splitext(config['filename'])

    engine = config['engine']

    custom_css = flask.Markup(_read_if_exists(talk_no_suffix, 'css', engine))

    custom_head_html = flask.Markup(_read_if_exists(talk_no_suffix, 'head.html', engine))

    custom_body_html = _read_if_exists(talk_no_suffix, 'body.html', engine)
    custom_body_html = flask.Markup(Template(custom_body_html).render(markdown=markdown))

    return flask.render_template('render.html',
                                 title=title,
                                 custom_css=custom_css,
                                 custom_head_html=custom_head_html,
                                 custom_body_html=custom_body_html,
                                 engine=config['engine'])


@blueprint.route('/images/<path:path>')
def serve_image(path):
    config = flask.current_app.config
    return flask.send_from_directory(config['imagedir'], path)


@blueprint.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
