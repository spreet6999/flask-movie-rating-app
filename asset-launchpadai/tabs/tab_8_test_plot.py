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

input_data = context.catalog.load('cleaned_sensor_data')

sensor_name = "sensor_49"
# texts = context.catalog.load('gensim_lda_texts')
# corpus = context.catalog.load('gensim_lda_corpus')
# dictionary = context.catalog.load('gensim_lda_dictionary')
# gensim_lda_model = context.catalog.load('gensim_lda_model')

# Load clean text
input_data[sensor_name+"_bucket"] = np.round(input_data[sensor_name])

count_table = input_data.groupby(sensor_name+"_bucket").agg({'timestamp': ['count'], "machine_status_bin": ['sum'] })
count_table = count_table.reset_index()
count_table.columns = ("bucket","total","positive")
count_table["incidence"] = count_table["positive"]/count_table["total"]

#arbitrary cutoff of 5 minimum readings for a value to not be an outlier
count_table=count_table[count_table["total"]>5]


fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    Scatter(x=count_table["bucket"], y=count_table["total"], name="Total Reads"),
    secondary_y=False,
)

fig.add_trace(
    Scatter(x=count_table["bucket"], y=count_table["incidence"], name="Downtime Rate"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text=sensor_name+" Total Reads vs Positive Incidence Rate by Sensor Reading"
)

# Set x-axis title
fig.update_xaxes(title_text="Sensor level buckets")

# Set y-axes titles
fig.update_yaxes(title_text="Total Reads", secondary_y=False)
fig.update_yaxes(title_text="% Downtime", secondary_y=True)


test = dcc.Markdown('''
This is a list
* **Item 1 has bold text** followed by plain text
* Some Markdown text with _italics_
  * Item 2a
  * Item 2b
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Sensor 49 Data Exploration",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
