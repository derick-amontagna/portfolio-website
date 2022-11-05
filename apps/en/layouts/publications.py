from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Publications
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Selected Publications and Preprints """, id="publications"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/en/publications.txt", "r").read()),
                style={"textAlign": "left"},
            )
        ),
    ]
)
