from dash import Dash
from dash_bootstrap_components.themes import FLATLY as theme

app = Dash(
    __name__,
    external_stylesheets=[theme],
    meta_tags=[{"name": "viewport", "content": "width=device-width",
     "initial-scale":"1.0", 
     "max-scale":"1.2",
     "minimum-scale":"0.5"}],
)
app.title = "Derick's Portfolio Website"
server = app.server


@server.route("/health/liveness/")
def liveness():
    """
    Checks server liveness.
    """
    return "alive", 200


@server.route("/health/readiness/")
def readiness():
    """
    Checks server readiness.
    """
    return "ready", 200
