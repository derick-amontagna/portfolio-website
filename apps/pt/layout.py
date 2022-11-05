from dash import html, dcc
import dash_bootstrap_components as dbc
import apps.pt.components as cp
from apps.style import CONTENT_STYLE


content = html.Div(id="page-content-pt", style=CONTENT_STYLE)


layout = html.Div([dcc.Location(id="url-pt"), cp.sidebar, content])
