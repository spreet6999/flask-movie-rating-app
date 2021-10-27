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

input_data = context.catalog.load('cleaned_sensor_data').reset_index().rename(columns = {'index':'timestamp'}) 

sensor_names = [column for column in input_data.columns if column.startswith("sensor")]
sensor_data = {}


for sensor_name in sensor_names:
    #for each sensor, calculate the histogram of sensor values
    # as well as what the distribution of machine status is at each sensor reading

    #use only whole values
    input_data[sensor_name+"_bucket"] = np.round(input_data[sensor_name])

    #count sensor readings
    count_table = input_data.groupby(sensor_name+"_bucket").agg({'timestamp': ['count'], "machine_status_bin": ['sum'] })
    count_table = count_table.reset_index()
    count_table.columns = ("bucket","total","positive")

    #count machine status down rate at each sensor reading
    count_table["incidence"] = count_table["positive"]/count_table["total"]

    #arbitrary cutoff of 5 minimum readings for a value to not be an outlier
    count_table=count_table[count_table["total"]>5]
    sensor_data[sensor_name]=count_table

#define the plots, creating two sets of values for each sensor ("trace"),
#one for the sensor value histogram
#one for the incidence rate for each sensor
def multi_plot(sensor_names,sensor_data_dict):
    fig = Figure()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    list_of_sensors = []

    for column in sensor_names:
        count_table = sensor_data_dict[column]
        fig.add_trace(
            Scatter(x=count_table["bucket"], y=count_table["total"], name="Total Reads",visible = False),
            secondary_y=False,
            
        )
        list_of_sensors.append(column)
        fig.add_trace(
            Scatter(x=count_table["bucket"], y=count_table["incidence"], name="Downtime Rate",visible = False),
            secondary_y=True,
        )
        list_of_sensors.append(column)
    fig.update_layout(
        title_text="Total Reads vs Positive Incidence Rate by Sensor Reading"
    )


    # Set x-axis title
    fig.update_xaxes(title_text="Sensor level buckets")

    # Set y-axes titles
    fig.update_yaxes(title_text="Total Reads", secondary_y=False)
    fig.update_yaxes(title_text="% Downtime", secondary_y=True)
    

    #for each sensor, create a button. Clicking on it will allow you to make the 
    #two traces for the sensor visible, but make the others invisible
    def create_layout_button(column):
        return dict(label = column,
            method = 'update',
            args = [{'visible': [x==column for x in list_of_sensors],
            'title': column,
            'showlegend': True}])

    fig.update_layout(
        updatemenus=[layout.Updatemenu(
            active = 0,
            buttons = [create_layout_button(column) for column in sensor_names]
            )
        ])
   
    
    return fig


fig = multi_plot(sensor_names,sensor_data)


test = dcc.Markdown('''
Sensor data vs outcome variable
- Sensor data aggregated by count of readings
- Outcome variable count aggregated by sensor data readings
Examples:
- Sensor 01 shows that downtime occurs most often when the readings of sensor 01 are below 43
- Sensor 49 shows that downtime occurs most often when the readings of sensor 49 are below 42 or above 130
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Sensor Data Exploration",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
