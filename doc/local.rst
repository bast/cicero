

Running a local web server
==========================

Sometimes you need to present your talk without an internet connection.
In this situation you can run a local web server.

First install the dependencies (you need a network connection for this step)::

  $ virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

Then start the server::

  $ python cicero.py

  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)


Serving local files
===================

Using a local server it is also no problem to serve your talk locally to see the
result before you push them to the repository::

  $ python cicero.py --file /home/user/my-talk/talk.md
