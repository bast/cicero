from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    arg = parser.add_argument

    arg('--file', '-f', dest='filename', help='serve a local file')
    arg('--engine', dest='engine', help='rendering engine', default='remark-0.13.0')
    arg('--debug', dest='debug', action='store_true', default=False)
    arg('--host', dest='host', default=os.environ.get('HOST', '127.0.0.1'))
    arg('--port', dest='port', type=int, default=int(os.environ.get('PORT', 5000)))

    return parser.parse_args()
