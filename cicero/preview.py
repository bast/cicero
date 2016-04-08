from flask import Blueprint

blueprint = Blueprint('preview', __name__)


@blueprint.route('/')
def home():
    import io
    from flask import current_app, render_template
    from .images import fix_images

    config = current_app.config

    with io.open(config['filename'], 'r', encoding='utf-8') as mkdfile:
        markdown = mkdfile.readlines()

    markdown = fix_images(markdown, 'images/')

    return render_template('slides.html', markdown=markdown)


@blueprint.route('/images/<path:path>')
def serve_image(path):
    from flask import send_from_directory, current_app
    config = current_app.config
    return send_from_directory(config['imagedir'], path)


@blueprint.errorhandler(404)
def page_not_found(e):
    from flask import render_template
    return render_template('404.html'), 404
