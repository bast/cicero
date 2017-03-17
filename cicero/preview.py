from flask import Blueprint

blueprint = Blueprint('preview', __name__)


@blueprint.route('/')
def home():
    import io
    import os
    from flask import current_app, render_template, render_template_string, request
    from .title import extract_title
    from .images import fix_images

    config = current_app.config

    with io.open(config['filename'], 'r', encoding='utf-8') as mkdfile:
        markdown = mkdfile.read()

    title = extract_title(markdown)
    markdown = fix_images(markdown, 'images/')

    style = request.args.get('style')
    if style is None:
        style = 'default'

#   mkd_path = os.path.dirname(os.path.realpath(config['filename']))
#   own_template_file = os.path.join(mkd_path, 'remark.html')
#   if os.path.isfile(own_template_file):
#       # own template file exists, we use it instead the default one
#       fd = blueprint.open_resource(own_template_file)
#       return render_template_string(fd.read().decode("utf-8"),
#                                     title=title,
#                                     markdown=markdown,
#                                     style=style)
#   else:
#       # default template
    return render_template('remark.html',
                           title=title,
                           markdown=markdown,
                           style=style,
                           engine='remark-0.13.0')  # FIXME hardcoded


@blueprint.route('/images/<path:path>')
def serve_image(path):
    from flask import send_from_directory, current_app
    config = current_app.config
    return send_from_directory(config['imagedir'], path)


@blueprint.errorhandler(404)
def page_not_found(e):
    from flask import render_template
    return render_template('404.html'), 404
