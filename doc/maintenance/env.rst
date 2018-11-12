

Running your own server
=======================

You can run your own Cicero instance on your own server. Cicero is a Flask app
and to serve it you should use a WSGI server for production.
The sources are open: https://github.com/bast/cicero


Environment variables
=====================

You will need to define ``CICERO_URL_BASE`` to the URL of your server. This sets the
URL base for generated links in the Markdown file finder.

As an example, for https://cicero.xyz we set::

  CICERO_URL_BASE=https://cicero.xyz
