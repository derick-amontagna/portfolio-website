# -*- coding: utf-8 -*-
import os
from dash import Dash, html
from dash_bootstrap_components.themes import FLATLY as theme
from pages import layout

app = Dash(__name__, external_stylesheets=[theme],  meta_tags=[{"name": "viewport", "content": "width=device-width"}]) 
app.title = "Derick's Portfolio Website"
server = app.server

app.layout = layout.layout

if __name__ == "__main__":
    port = os.getenv("PORT", "8050")
    debug = os.getenv("DEBUG") == "true"
    app.run_server(host="0.0.0.0", port=port, debug=True) # http://127.0.0.1:8050
