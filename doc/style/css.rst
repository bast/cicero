

How to use own CSS
==================

If you place a file in the same path as your talk, with the same name as your
talk, and only replace the ".md" suffix by ".css". Then the rendering engine
will use this file and include it as the last CSS file:
https://github.com/bast/cicero/blob/master/cicero/templates/render.html#L14-L16

In other words, if your talk is called "talk.md" and you want to customize CSS,
place a file called "talk.css" in the same place as your "talk.md".

With this you can even override CSS directives and style your slides to your heart's content.
