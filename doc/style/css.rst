

How to use own CSS
==================

If you place a file in the same path as your talk, with the same name as your
talk, and only replace the ``.md`` suffix by ``.css``. Then the rendering engine
will use this file:
https://github.com/bast/cicero/blob/master/cicero/templates/render.html#L11-L13

In other words, if your talk is called ``mytalk.md`` and you want to customize CSS,
place a file called ``mytalk.css`` in the same place as your ``mytalk.md``.

With this you can even override CSS directives and style your slides to your
heart's content.

Example: https://github.com/bast/cicero/tree/master/demo/remark/styling
