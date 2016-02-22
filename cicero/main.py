import os
import argparse
from .app import app
from . import git
from . import preview


def parse_args():
    parser = argparse.ArgumentParser()
    arg = parser.add_argument

    arg('--file', '-f', dest='filename', help='Serve local file')
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '0.0.0.0'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()


def main():
    args = parse_args()

    if args.filename:
        app.config['filename'] = args.filename
        app.config['imagedir'] = os.path.dirname(args.filename)
        app.register_blueprint(preview.blueprint)
    else:
        app.register_blueprint(git.blueprint)

    app.debug = args.debug

    app.run(host=args.host, port=args.port)
