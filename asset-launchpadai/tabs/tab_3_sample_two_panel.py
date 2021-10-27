# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import app  # other objects such as "indicator" can be imported and used it

right_content = template_obj.blank_textbox(
    content=html.Ul([
        html.Li(children=[html.B('First major point: '),
                          'description of first major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point'),
            html.Li('Third minor point')
        ]),
        html.Li(children=[html.B('Second major point: '),
                          'description of second major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point')
        ]),
        html.Li(children=[html.B('Third major point: '),
                          'description of third major']),
        html.Li(children=[html.B('Fourth major point: '),
                          'description of fourth major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point'),
            html.Li('Third minor point')
        ]),
        html.Li(children=[html.B('Fifth major point: '),
                          'description of fifth major'])
    ])
)

# chart stages data
values = [18873, 10553, 5443, 3703, 1308, 634]
phases = ['Visit', 'Sign-up', 'Selection', 'Purchase', 'Review', 'Return']

# color of each funnel section
colors = ["#051C2C", "#033F5E", "#026290", "#0185C2", "#00A3D0", "#00A9F4"]

figure = chart_template.funnel_chart(values=values, phases=phases, colors=colors)

layout = page_template.layout_two_panel(page_lead="Test page lead",
                                        left_panel_content=template_obj.graph_content(
                                            figure=figure),
                                        right_panel_content=template_obj.title_textbox(title="Key points;", content=right_content)
                                        )
