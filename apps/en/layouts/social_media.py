from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Social Media
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Social Media """, id="redeSocial"), style={"textAlign": "left"}
            )
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/social.txt", "r").read()), style={"textAlign": "left"})
        ),
    ]
)
