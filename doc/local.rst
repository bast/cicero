

Running the app locally
=======================

You can preview your changes locally and also present your talk
without relying on https://cicero.xyz::

  $ pip install cicero
  $ cicero --file /home/user/my-talk/talk.md


Available options
-----------------

::

  $ cicero --help

  usage: cicero.py [-h] [--file FILENAME] [--engine ENGINE] [--debug]
                   [--host HOST] [--port PORT]

  optional arguments:
    -h, --help            show this help message and exit
    --file FILENAME, -f FILENAME
                          serve a local file (default: None)
    --engine ENGINE       rendering engine (available: remark-0.13.0,
                          remark-0.14.0, remark-legacy, reveal.js-3.7.0)
                          (default: remark-0.14.0)
    --debug
    --host HOST
    --port PORT
