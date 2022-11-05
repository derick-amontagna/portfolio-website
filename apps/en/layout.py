from dash import html, dcc
import apps.en.components as cp
from apps.style import CONTENT_STYLE


content = html.Div(id="page-content-en", style=CONTENT_STYLE)


layout = html.Div([dcc.Location(id="url-en"), cp.sidebar, content])
