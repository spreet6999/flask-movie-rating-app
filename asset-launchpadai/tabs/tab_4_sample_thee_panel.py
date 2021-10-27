# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
import numpy as np
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import app  # other objects such as "indicator" can be imported and used it

test = dcc.Markdown('''
This is a list
* **Item 1 has bold text** followed by plain text
* Some Markdown text with _italics_
  * Item 2a
  * Item 2b
''')

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']
colors = [chart_template.Purple, chart_template.Orange, chart_template.Cyan]

figure_1 = chart_template.dist_hist_chart(hist_data=hist_data, group_labels=group_labels, colors=colors)

# data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

x_vals = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

y_vals = [high_2000, low_2000, high_2007, low_2007, high_2014, low_2014]
trace_names = ['High 2014', 'Low 2014', 'High 2007', 'Low 2007', 'High 2000', 'Low 2000']
dash_types = [None, 'dash', 'dot', None, 'dash', 'dot']
color_vals = [chart_template.Deep_Blue, chart_template.Pale_Blue, chart_template.Dark_Gray, chart_template.Mid_Gray,
              chart_template.Cyan, chart_template.Electric_Blue]

figure_2 = chart_template.line_chart_plot(title="Average Temps in NYC", y_vals=y_vals, trace_names=trace_names,
                                          x_vals=x_vals, dash_types=dash_types, color_vals=color_vals)

layout = page_template.layout_thee_panel(page_lead="Test page lead",
                                         left_panel_content=template_obj.graph_content(
                                             figure=figure_1),
                                         middle_panel_content=template_obj.graph_content(
                                             figure=figure_2),
                                         right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                        content=test)
                                         )
