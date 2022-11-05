from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Social Media
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Rede Sociais """, id="redeSocial"), style={"textAlign": "left"}
            )
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/social.txt", "r").read()), style={"textAlign": "left"})
        ),
    ]
)
