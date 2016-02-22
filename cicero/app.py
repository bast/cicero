import os
import flask


def _get_subdir(dirname):
    return os.path.join(os.path.dirname(__file__), dirname)


app = flask.Flask('Cicero',
                  template_folder=_get_subdir('templates'),
                  static_folder=_get_subdir('static'))


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('404.html'), 404
