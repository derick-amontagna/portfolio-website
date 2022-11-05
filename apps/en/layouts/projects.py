from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Projects
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Projects """, id="projects"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/en/projects.txt", "r").read()), style={"textAlign": "left"}
            )
        )
    ]
)
