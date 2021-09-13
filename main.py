from cicero.app import app
from cicero import git

app.register_blueprint(git.blueprint)
