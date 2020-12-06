import io
import os
import flask
import requests
from jinja2 import Template


def _read_if_exists(url_prefix, custom_prefix, suffix, engine):

    if url_prefix is None:
        custom_file_name = custom_prefix + "." + suffix
        if os.path.isfile(custom_file_name):
            with io.open(custom_file_name, "r") as f:
                return f.read()
    else:
        url = url_prefix + "/" + custom_prefix + "." + suffix
        response = requests.get(url)
        if response.status_code != 404:
            return response.text

    vendor_file_name = os.path.join(
        os.path.dirname(__file__), "static", "engines", engine, "vendor." + suffix
    )
    if os.path.isfile(vendor_file_name):
        with io.open(vendor_file_name, "r") as f:
            return f.read()

    return ""


def render(engine, url_prefix, md_file_prefix, markdown):

    engine_root = flask.url_for("static", filename="engines/" + engine)

    # flask.Markup to disable autoescaping
    custom_css = flask.Markup(
        _read_if_exists(url_prefix, md_file_prefix, "css", engine)
    )

    _tmp = _read_if_exists(url_prefix, md_file_prefix, "head.html", engine)
    custom_head_html = flask.Markup(Template(_tmp).render(engine_root=engine_root))

    _tmp = _read_if_exists(url_prefix, md_file_prefix, "body.html", engine)
    custom_body_html = flask.Markup(
        Template(_tmp).render(markdown=markdown, engine_root=engine_root)
    )

    return flask.render_template(
        "render.html",
        title="presentation",
        custom_css=custom_css,
        custom_head_html=custom_head_html,
        custom_body_html=custom_body_html,
        engine=engine,
    )
