from dash import html, dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        # Skills
        dbc.Row(dbc.Col(dcc.Markdown("""## Habilidades """, id="habilidades"), style={"textAlign": "left"})),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/skills.txt", "r").read()), style={"textAlign": "left"})
        )
    ]
)
