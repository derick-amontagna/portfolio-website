# -*- coding: utf-8 -*-
from dash import Dash
from dash.long_callback import DiskcacheLongCallbackManager
from dash_bootstrap_components.themes import FLATLY as theme
import diskcache

cache = diskcache.Cache("./cache")
long_callback_manager = DiskcacheLongCallbackManager(cache)
app = Dash(__name__, external_stylesheets=[theme], long_callback_manager=long_callback_manager)
app.title = "Derick's Portfolio Website"
server = app.server
