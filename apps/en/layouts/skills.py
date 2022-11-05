from dash import dcc
import dash_bootstrap_components as dbc


layout = dbc.Container(
    [
        # Skills
        dbc.Row(dbc.Col(dcc.Markdown("""## Skills """, id="skills"), style={"textAlign": "left"})),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/skills.txt", "r").read()), style={"textAlign": "left"})
        ),
    ]
)
