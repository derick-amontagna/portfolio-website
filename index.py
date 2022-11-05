# -*- coding: utf-8 -*-
import os
from dash import html
from app import app
from apps import pages_front
import apps.en.layout
import apps.en.callbacks
import apps.pt.layout
import apps.pt.callbacks

app.layout = pages_front.layout

app.validation_layout = html.Div(
    [
        apps.pages_front.layout,
        apps.en.layout.layout,
        apps.pt.layout.layout,
    ]
)

if __name__ == "__main__":
    port = os.getenv("PORT", "8050")
    debug = os.getenv("DEBUG") == "true"
    app.run_server(host="0.0.0.0", port=port, debug=True)  # http://localhost:8050
