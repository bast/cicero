

v3
==

This API is the future::

  /v3/<engine>/<engine_version>/<repo>/<branch>/<path>/

Example:

  /v3/remark/0.14.0/github.com/bast/cicero/master/demo/talk.md


v2
==

This API is currently the default::

  /v2/remark/github/<namespace>/<repo>/<branch>/<path>/

Example:

  /v2/remark/github/bast/cicero/master/demo/talk.md


v1
==

This API is deprecated but supported::

  /v1/github/<namespace>/<repo>/<branch>/<path>/remark/
