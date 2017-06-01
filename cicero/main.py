def parse_args():
    from argparse import ArgumentParser
    import os

    parser = ArgumentParser()
    arg = parser.add_argument

    arg('--file', '-f', dest='filename', help='serve a local file')
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '0.0.0.0'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()


def main():
    import os
    import sys
    from .app import app
    from . import git
    from . import preview

    args = parse_args()

    if args.filename:

        if not os.path.isfile(args.filename):
            sys.stderr.write('ERROR: file {0} not found\n'.format(args.filename))
            sys.exit(1)

        app.config['filename'] = args.filename
        app.config['imagedir'] = os.path.dirname(args.filename)
        app.register_blueprint(preview.blueprint)
    else:
        git.set_url_base(args.host, args.port)
        app.register_blueprint(git.blueprint)

    app.debug = args.debug

    app.run(host=args.host, port=args.port)
