from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Publications
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Seleção de publicações """, id="publicacao"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/pt/publications.txt", "r").read()),
                style={"textAlign": "left"},
            )
        ),
    ]
)
