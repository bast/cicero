from argparse import ArgumentParser
import os


def parse_args():
    parser = ArgumentParser()
    arg = parser.add_argument

    arg('--file', '-f', dest='filename', help='serve a local file')
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '0.0.0.0'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()
