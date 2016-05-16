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
