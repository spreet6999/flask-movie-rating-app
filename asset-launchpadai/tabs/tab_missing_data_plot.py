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

sensor_data = context.catalog.load('example_sensor_data')

#count number NAs by columns
empty_values = sensor_data.apply(lambda x: x.isnull().sum(), axis='rows')

#determine missing percent
total_missing =  (empty_values/len(sensor_data)).to_frame().reset_index()
total_missing.columns = ["sensor","missing_rate"]

#graph missing percent by sensor
fig = px.bar(total_missing, x='sensor', y='missing_rate')


test = dcc.Markdown('''
Number of missing data values by sensor
- Sensor 15 is missing most of its data and we should consider excluding
- Sensor 50 and 51 could also be excluded due to lack of data
- Sensors 06, 07, 08, and 09 should be examined in case of flaws
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Missing Sensor Data",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
