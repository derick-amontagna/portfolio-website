from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Work Experience
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Work Experience """, id="work"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/en/workExperience.txt", "r").read()),
                style={"textAlign": "left"},
            )
        )
    ]
)
