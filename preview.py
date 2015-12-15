import os
import sys
import io
import flask
import urllib
import re
from argparse import ArgumentParser

from images import fix_images


# ------------------------------------------------------------------------------

app = flask.Flask(__name__)

# ------------------------------------------------------------------------------


@app.route('/')
def home():
    with io.open(app.config['filename'], 'r', encoding='utf-8') as mkdfile:
        markdown = mkdfile.readlines()

    markdown = ''.join(fix_images(markdown, 'images/'))
    
    return flask.render_template('slides.html', markdown=markdown)

# ------------------------------------------------------------------------------


@app.route('/images/<path:path>')
def serve_image(path):
    return flask.send_from_directory(app.config['image_dir'], path)

# ------------------------------------------------------------------------------


def parse_args():
    parser = ArgumentParser()
    arg = parser.add_argument

    arg('filename', nargs=1)
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '0.0.0.0'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()
    
# ------------------------------------------------------------------------------


if __name__ == '__main__':
    args = parse_args()
    app.config['filename'] = args.filename[0]
    app.config['image_dir'] = os.path.dirname(args.filename[0])
    app.debug = args.debug

    app.run(host=args.host, port=args.port)
