from packaging.version import parse
from collections import namedtuple

__version__ = '0.1.1b1'

version_info = namedtuple('version_info', ['major', 'minor', 'micro'])

_p = parse(__version__)

version_info.major, version_info.minor, version_info.micro = _p.release
