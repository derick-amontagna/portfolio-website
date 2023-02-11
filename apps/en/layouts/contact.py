from dash import dcc
import dash_bootstrap_components as dbc

layout = dbc.Container(
    [
        # Contact
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""## Contact """, id="contact"), style={"textAlign": "left"}
            )
        ),
        dbc.Row(
            dbc.Col(dcc.Markdown(open("data/contact.txt", "r").read()), style={"textAlign": "left"})
        ),
    ]
)
