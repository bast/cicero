import os
import sys
from .app import app
from . import git
from . import preview
from .cli import parse_args


def main():
    args = parse_args()

    if args.filename:

        if not os.path.isfile(args.filename):
            sys.stderr.write("ERROR: file {0} not found\n".format(args.filename))
            sys.exit(1)

        app.config["filename"] = args.filename
        app.config["engine"] = args.engine
        app.config["imagedir"] = os.path.dirname(args.filename)
        app.register_blueprint(preview.blueprint)
    else:
        git.set_url_base(args.host, args.port)
        app.register_blueprint(git.blueprint)

    app.debug = args.debug

    app.run(host=args.host, port=args.port)
