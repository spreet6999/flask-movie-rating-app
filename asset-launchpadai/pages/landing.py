# -*- coding: utf-8 -*-
# import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# import pandas as pd
# import plotly.plotly as py
# from plotly import graph_objs as go
# import math
from app import app, project_name, logo, app_prefix, host, app_port
# from apps import dynamic_test
from tabs import tab_1_exec_sum


landing_page_layout = html.Div([
    # This is the overall header for the page - you can modify the logo name and content from tha app.py file
    # other properties like background color can be set in the CSS file which is in the assets folder
    html.Div(tab_1_exec_sum.layout)
])

