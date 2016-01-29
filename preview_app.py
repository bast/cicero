import io
import flask

from images import fix_images

app = flask.Flask('Cicero Preview')


@app.route('/')
def home():
    with io.open(app.config['filename'], 'r', encoding='utf-8') as mkdfile:
        markdown = mkdfile.readlines()

    markdown = ''.join(fix_images(markdown, 'images/'))

    return flask.render_template('slides.html', markdown=markdown)


@app.route('/images/<path:path>')
def serve_image(path):
    return flask.send_from_directory(app.config['image_dir'], path)


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
