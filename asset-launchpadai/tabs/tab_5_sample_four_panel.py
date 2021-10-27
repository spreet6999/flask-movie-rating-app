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

data = pd.DataFrame({'2012': np.random.randn(200),
                     '2013': np.random.randn(200) + 1})

figure_1 = chart_template.dist_hist_pandas_chart(data=data,
                                                 bin_size=0.1)

figure_2 = chart_template.dist_hist_pandas_chart(data=data,
                                                 bin_size=0.25)

figure_3 = chart_template.dist_hist_pandas_chart(data=data,
                                                 bin_size=0.55)

layout = page_template.layout_four_panel(page_lead="Test page lead",
                                         left_panel_content=template_obj.graph_content(
                                             figure=figure_1),
                                         middle_left_panel_content=template_obj.graph_content(
                                             figure=figure_2),
                                         middle_right_panel_content=template_obj.graph_content(
                                             figure=figure_3),
                                         right_panel_content=template_obj.title_textbox(title='Key Points:',
                                                                                        content=test)
                                         )
