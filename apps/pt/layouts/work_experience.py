from dash import html, dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Work Experience
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Experiência de trabalho """, id="experienciaDeTrabalho"),
                style={"textAlign": "left"},
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Markdown(open("data/pt/workExperience.txt", "r").read()),
                style={"textAlign": "left"},
            )
        )
    ]
)
