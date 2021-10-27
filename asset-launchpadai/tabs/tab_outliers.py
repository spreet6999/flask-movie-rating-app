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

input_data_raw = context.catalog.load('cleaned_sensor_data')


#CURRENTLY NOT WORKING too much memory used

def multi_plot_13(sensor_names,input_data):
    fig = Figure()


    list_of_sensors = []

    for column in sensor_names:
        fig.add_trace(
        Box( y=input_data[column], visible=True),
        )

    
    fig.update_layout(
    title_text="Outliers by Sensor"
    )


    

    # def create_layout_button(column):
    #     return dict(label = column,
    #         method = 'update',
    #         args = [{'visible': [x==column for x in sensor_names],
    #         'title': column,
    #         'showlegend': True}])

    # fig.update_layout(
    #     updatemenus=[layout.Updatemenu(
    #         active = 0,
    #         buttons = [create_layout_button(column) for column in sensor_names]
    #         )
    #     ])
    # fig.update_layout(
    #     visible=[False for column in sensor_names]
    # )
    
    return fig

sensor_names = [column for column in input_data_raw.columns if column.startswith("sensor")]

fig = multi_plot_13(sensor_names,input_data_raw)


test = dcc.Markdown('''
This is a list
* **Item 1 has bold text** followed by plain text
* Some Markdown text with _italics_
  * Item 2a
  * Item 2b
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Outliers",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
