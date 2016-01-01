import os
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    arg = parser.add_argument

    arg('--file', '-f', dest='filename', help='Serve local file')
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '0.0.0.0'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.filename:
        from preview_app import app
        app.config['filename'] = args.filename
        app.config['image_dir'] = os.path.dirname(args.filename)
    else:
        from github_app import app

    app.debug = args.debug

    app.run(host=args.host, port=args.port)
