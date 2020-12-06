from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import os
import glob
import ntpath


def _get_list_of_engines():
    engines = []
    for path in glob.glob(
        os.path.join(os.path.dirname(__file__), "static", "engines", "*")
    ):
        engines.append(ntpath.basename(path))
    return sorted(engines)


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    arg = parser.add_argument
    engines = ", ".join(_get_list_of_engines())

    arg("--file", "-f", dest="filename", help="serve a local file")
    arg(
        "--engine",
        dest="engine",
        help="rendering engine (available: {0})".format(engines),
        default="remark-0.14.0",
    )
    arg("--debug", dest="debug", action="store_true", default=False)
    arg("--host", dest="host", default=os.environ.get("HOST", "127.0.0.1"))
    arg("--port", dest="port", type=int, default=int(os.environ.get("PORT", 5000)))

    return parser.parse_args()
