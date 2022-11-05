from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Projects
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Projetos """, id="projetos"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/pt/projects.txt", "r").read()), style={"textAlign": "left"}
            )
        )
    ]
)
