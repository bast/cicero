

How to use your own CSS
=======================

If you place a file in the same path as your talk, with the same name as your
talk, and only replace the ``.md`` suffix by ``.css``. Then the rendering engine
will use this file:
https://github.com/bast/cicero/blob/main/cicero/templates/render.html#L11-L13

In other words, if your talk is called ``mytalk.md`` and you want to customize CSS,
place a file called ``mytalk.css`` in the same place as your ``mytalk.md``.

With this you can even override CSS directives and style your slides to your
heart's content.

Example: https://github.com/bast/cicero/tree/main/demo/remark/styling


Images
======

You can either include images the
`Markdown way <https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#images>`_::

  ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

  ![alt text](path/myimage.jpg "Local image")

or the HTML way::

  <img src="file.jpg" style="height: 450px;"/>


Background image
================


remark
------

Setting and changing the background image is nicely documented here:
https://github.com/gnab/remark/wiki/Markdown#background-image


How to customize everything
===========================

You want to change looks and fonts? CSS is not enough? Perhaps you need an
external JavaScript library?

You can place ``*.head.html`` and/or ``*.body.html`` alongside your ``*.md`` slides.
In these files you can do and change almost everything:
https://github.com/bast/cicero/blob/main/cicero/templates/render.html.

To get inspired of what is in these by default and what can be changed, please
browse https://github.com/bast/cicero/tree/main/cicero/static/engines.


Math equations
==============

Here is an example:
https://github.com/bast/cicero/tree/main/demo/remark/equations
