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
from pages import tab_1_exec_sum, tab_2_test_plot, tab_3_word_frequency_plot, tab_4_topic_dist_plot, \
    tab_5_t_sne_scatter_plot, tab_6_explore_topic_plot, tab_7_topic_word_importance_plot

syslog_layout = html.Div([    
    # This is the overall header for the page - you can modify the logo name and content from tha app.py file
    # other properties like background color can be set in the CSS file which is in the assets folder
    html.Div([

        html.Span(project_name, className='app-title'),
        
        html.Div(
            html.Img(
                src=app.get_asset_url(logo),
                height="100%"),
            style={"float": "right", "height": "100%"})
    ],
        className="row header"
    )
    
    ])
