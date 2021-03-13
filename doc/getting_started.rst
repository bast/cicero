

Getting started in 5 minutes
============================

Place the following Markdown file on https://github.com or https://gitlab.com,
perhaps as ``mytalk.md``::

  class: center, middle

  # Simple example presentation

  ## Author

  ---

  ## Another slide

  Try **F** and **P** keys.

  - A bullet point
  - Another convincing argument

  ---

  ## Code blocks are no problem

  Here we have some Python code:

  ```python
  from itertools import cycle

  fizz = cycle(['', '', 'Fizz'])
  buzz = cycle(['', '', '', '', 'Buzz'])

  for i in range(1, 101):
      print((next(fizz) + next(buzz)) or i)
  ```

  [Source](https://github.com/olemb/nonsense/blob/master/fizzbuzz/itertools_cycle.py)

  ---

  ## Images

  An image fetched from the web:

  ![Sample image](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/The_Young_Cicero_Reading.jpg/316px-The_Young_Cicero_Reading.jpg)

Let us assume your talk is on (replace ``<namespace>`` and ``<repository>``)::

  https://github.com/<namespace>/<repository>/mytalk.md

You can now visit (replace ``<namespace>`` and ``<repository>``)::

  https://cicero.xyz/v3/remark/0.14.0/github.com/<namespace>/<repository>/main/mytalk.md

Of course you can reference another branch or tag or hash than ``main``.

If you like https://revealjs.com better, then check https://github.com/bast/cicero/tree/main/demo/reveal.js.
