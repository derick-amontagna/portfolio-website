import dash_bootstrap_components as dbc
from dash import html
from apps.style import SIDEBAR_STYLE


image_path = "assets\\github.png"
sidebar = html.Div(
    [
        html.H2("Derick Abreu Montagna", className="display-4"),
        html.Hr(),
        html.P("Everything about me is here! :)", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Education", href="/Education", active="exact"),
                dbc.NavLink("Publications", href="/Publications", active="exact"),
                dbc.NavLink("Work Experience", href="/Work-Experience", active="exact"),
                dbc.NavLink("Skills", href="/Skills", active="exact"),
                dbc.NavLink("Projects", href="/Projects", active="exact"),
                dbc.NavLink("Social Media", href="/Social-Media", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
        html.Br(),
        dbc.Alert(
            [
                html.Img(src=image_path, style={"height": "10%", "width": "10%"}),
                html.A(
                    "   Portfolio Source Code",
                    href="https://github.com/derick-amontagna/portfolio-website",
                    className="link",
                ),
            ],
            color="light",
            style={"marginBottom": "1em"},
        ),
    ],
    style=SIDEBAR_STYLE,
)
