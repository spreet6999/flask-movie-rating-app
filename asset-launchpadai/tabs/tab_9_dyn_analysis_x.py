# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import app  # other objects such as "indicator" can be imported and used it

# data that is used in the the dynamic plot
df = pd.read_csv('data/indicators.csv')

available_indicators = df['Indicator Name'].unique()
controls_val, dyn_graph_val = chart_template.create_dyn_graph(data=df,
                                                              x_cols=available_indicators,
                                                              # x_cols=['Fertility rate, total (births per woman)'],
                                                              x_cols_value='Fertility rate, total (births per woman)',
                                                              y_cols=available_indicators,
                                                              # y_cols=['Life expectancy at birth, total (years)'],
                                                              y_cols_val='Life expectancy at birth, total (years)',
                                                              filter_col='Year',
                                                              filter_type='drop_down',
                                                              chart_type_toggle=True)

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Test page lead",
                                          left_panel_content=dyn_graph_val,
                                          right_panel_content=controls_val,
                                          )
