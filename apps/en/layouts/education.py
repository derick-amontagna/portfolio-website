from dash import html, dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        # Education
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Education """, id="education"), style={"textAlign": "left"})
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/en/education.txt", "r").read()), style={"textAlign": "left"}
            )
        )
    ]
)
