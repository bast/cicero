

v3
==

This API is currently the default::

  /v3/<engine>/<engine_version>/<repo>/<branch>/<path>

Examples with `files on GitHub <https://github.com/bast/cicero/tree/main/demo>`__:

- https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/main/demo/remark/simple/talk.md
- https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/main/demo/remark/styling/talk.md
- https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/main/demo/remark/equations/talk.md
- https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/main/demo/remark/original/talk.md
- https://cicero.xyz/v3/remark/0.14.0/github.com/bast/cicero/main/demo/remark/header-footer/talk.md
- https://cicero.xyz/v3/reveal.js/3.7.0/github.com/bast/cicero/main/demo/reveal.js/talk.md

Examples with `files on GitLab <https://gitlab.com/bast/cicero-example/tree/master/demo>`__:

- https://cicero.xyz/v3/remark/0.14.0/gitlab.com/bast/cicero-example/master/demo/remark/simple/talk.md
- https://cicero.xyz/v3/remark/0.14.0/gitlab.com/bast/cicero-example/master/demo/remark/styling/talk.md
- https://cicero.xyz/v3/remark/0.14.0/gitlab.com/bast/cicero-example/master/demo/remark/equations/talk.md
- https://cicero.xyz/v3/remark/0.14.0/gitlab.com/bast/cicero-example/master/demo/remark/original/talk.md
- https://cicero.xyz/v3/reveal.js/3.7.0/gitlab.com/bast/cicero-example/master/demo/reveal.js/talk.md


v2
==

This API is the past but still supported::

  /v2/remark/github/<namespace>/<repo>/<branch>/<path>

Example: https://cicero.xyz/v2/remark/github/bast/cicero/main/demo/remark/original/talk.md


v1
==

This API is deprecated since it does not allow talks in subdirectories::

  /v1/github/<namespace>/<repo>/<branch>/<path>/remark/
