from .app import app
from . import git

app.register_blueprint(git.blueprint)
