import os

from dash import html

from app import app
from app import server  # pylint: disable=W0611


#app.layout = navigation_bar.layout

app.validation_layout = html.Div(
    [
        #navigation_bar.layout,
        # pages
    ]
)


if __name__ == "__main__":
    port = os.getenv("PORT", "8050")
    debug = os.getenv("DEBUG") == "true"
    app.run_server(host="0.0.0.0", port=port, debug=debug)
