from dash import html, dcc
import dash_bootstrap_components as dbc


image_path = "assets/indice.png"

layout = dbc.Container(
    [
        # Title
        dbc.Row(
            dbc.Col(
                dcc.Markdown("""# Derick Abreu Montagna, ElecEng"""), style={"textAlign": "center"}
            )
        ),
        # Resume
        dbc.Row(dbc.Col(dcc.Markdown("""##### *Resumo* """), style={"textAlign": "center"})),
        dbc.Row(
            dbc.Col(
                html.Img(src=image_path, style={"--m": "8", "--tan": "0.41"}),
                style={"textAlign": "center"},
            )
        ),
        # Summary
        dbc.Row(
            dbc.Col(dcc.Markdown("""## Sumário """, id="sumario"), style={"textAlign": "left"})
        ),
        dbc.Row(dbc.Col(dcc.Markdown(open("data/pt/summary.txt", "r").read()))),
    ]
)
