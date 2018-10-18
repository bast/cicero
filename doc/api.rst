
The API currently only supports
`remark <https://github.com/gnab/remark>`__,
but in future
we plan to support also other rendering engines.


v3
==

This API is the future::

  /v3/<engine>/<engine_version>/<repo>/<branch>/<path>/

Examples:

- GitHub: https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/master/demo/talk.md/
- GitLab: https://cicero.xyz/v3/remark/0.14.0/gitlab.com/bast/cicero-example/master/demo/talk.md/


v2
==

This API is currently the default::

  /v2/remark/github/<namespace>/<repo>/<branch>/<path>/

Example: https://cicero.xyz/v2/remark/github/bast/cicero/master/demo/talk.md


v1
==

This API is deprecated since it does not allow talks in subdirectories::

  /v1/github/<namespace>/<repo>/<branch>/<path>/remark/
