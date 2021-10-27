# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
from random import random
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
#from plotly import graph_objs as go
import plotly.express as px
from apps import template_obj, chart_template, page_template
from plotly.graph_objs import *
from app import app, context  # other objects such as "indicator" can be imported and used it
from plotly.subplots import make_subplots


import numpy as np

sensor_data = context.catalog.load('cleaned_sensor_data')

#correlation matrix between all sensors
corr_matrix = sensor_data.corr()

row_list = corr_matrix.values.tolist()


fig = Figure(data=Heatmap(
                   z=row_list,
                   x=corr_matrix.columns.values,
                   y=corr_matrix.index.values,
                   hoverongaps = False))


test = dcc.Markdown('''
Correlation level between each pair of sensor data
- Sensors 16-26 look heavily correlated to each other and deserve consideration for pruning
- Sensors 28-33 look very correlated to each other, and could also be pruned
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Missing Sensor Data",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
