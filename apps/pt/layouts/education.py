from dash import html, dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        # Education
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Educação """, id="educacao"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/pt/education.txt", "r").read()), style={"textAlign": "left"}
            )
        )
    ]
)
