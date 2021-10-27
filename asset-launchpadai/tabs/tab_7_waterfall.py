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

test = dcc.Markdown('''
This is a list
* **Item 1 has bold text** followed by plain text
* Some Markdown text with _italics_
  * Item 2a
  * Item 2b
''')
x_val = ["2016EOY", "Q1 2017", "Q2 2017", "Q3 2017", "Q4 2017", '2017 EOY', "Q1 2018", "Q2 2018", "Q3 2018",
         " Q4 2018", '2018 EOY', "Q1 2019", "Q2 2019", "Q3 2019", " Q4 2019", '2019 EOY']
in_values = [10, 20, 30, -10, 15, 'e', 10, 20, -40, 25, 'tot', 10, 20, -40, -5, 'tot']
plot_title = "Profit and loss statement"

figure = chart_template.waterfall_chart(title=plot_title,
                                        x_val=x_val,
                                        in_values=in_values)

layout = page_template.layout_left_small(page_lead="Test page lead",
                                         left_panel_content=template_obj.title_textbox(title="New Title",
                                                                                       content=test),
                                         right_panel_content=template_obj.graph_content(
                                             figure=figure),
                                         )
