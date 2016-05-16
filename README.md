[![Build Status](https://travis-ci.org/bast/cicero.svg?branch=master)](https://travis-ci.org/bast/cicero/builds)


# Cicero

Serving slides written in markdown: http://cicero.xyz

In the background uses [remark](https://github.com/gnab/remark),
a simple, in-browser, markdown-driven slideshow tool
created by [Ole Petter Bang](https://github.com/gnab).


## Contributors

- [Ole Martin Bjørndalen](https://github.com/olemb) (local preview and Blueprint solution)
- [Roberto Di Remigio](https://github.com/robertodr) (MathJax support)


## API

### v1 (deprecated but supported)

- Does not support files in subdirectories.
```
/v1/github/<namespace>/<repo>/<branch>/<file>/remark/
```


### v2

- Supports files in subdirectories.
```
/v2/remark/github/<namespace>/<repo>/<branch>/<file>/
```


## Environment variables

`CICERO_URL_BASE`: defines the URL base for generated links in the Markdown file finder


## Template customization

It is possible to use your own template for customization and branding.  For
this place a file called "remark.html" in the same location as the Markdown
file which contains your slides. If such a file exists, it will be used instead
of the [default template](../master/cicero/templates/remark.html). Make sure to
use the variables "title" and "markdown" in your custom template. Apart from
that you have full liberty to employ own CSS and JavaScript.
