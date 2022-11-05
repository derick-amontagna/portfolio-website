from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

from app import app
import apps.en.layout as en
import apps.pt.layout as pt

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            en.layout
        ]
    ),
    className="mt-3",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            pt.layout
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="en", tab_style={"marginLeft": "auto"}),
        dbc.Tab(tab2_content, label="pt"),
    ]
)

layout = html.Div([tabs])