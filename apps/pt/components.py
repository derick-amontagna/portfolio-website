import dash_bootstrap_components as dbc
from dash import html
from apps.style import SIDEBAR_STYLE

sidebar = html.Div(
    [
        html.H2("Derick Abreu Montagna", className="display-4"),
        html.Hr(),
        html.P(
            "Tudo sobre mim está por aqui! :)", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Inicio", href="/", active="exact"),
                dbc.NavLink("Educação", href="/Education", active="exact"),
                dbc.NavLink("Publicações", href="/Publications", active="exact"),
                dbc.NavLink("Experiencia de trabalho", href="/Work-Experience", active="exact"),
                dbc.NavLink("Habilidades", href="/Skills", active="exact"),
                dbc.NavLink("Projetos", href="/Projects", active="exact"),
                dbc.NavLink("Rede Sociais", href="/Social-Media", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
