

Exporting slides to PDF
=======================

The to my knowledge best way to export slides to PDF is using
https://github.com/astefanutti/decktape.

First install the tool following https://github.com/astefanutti/decktape#install,
then you can export slides, e.g.::

  $ decktape https://example.org/my-slides.md/ my-slides.pdf

If you prefer not to install it but have Singularity installed, you can do this instead::

  $ singularity pull docker://astefanutti/decktape
  $ ./decktape_latest.sif https://example.org/my-slides.md/ my-slides.pdf
