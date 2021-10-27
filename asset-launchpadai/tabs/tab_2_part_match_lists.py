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
import plotly.figure_factory as ff
# import plotly.plotly as py
from plotly import graph_objs as go
import plotly.express as px
from apps import template_obj, chart_template, page_template
from app import df_cleaned, portfolio_list, \
    matchings_pkl  # other objects such as "indicator" can be imported and used it
import numpy as np
from src.portfolio_ai.nodes import post_processing_and_analysis

# brand_list = df_cleaned[df_cleaned['Portfolio'] == portfolio_list[1]]['Brand'].unique()
# df_cleaned_select = df_cleaned[(df_cleaned['Portfolio'] == portfolio_list[1]) & (df_cleaned['Brand'] == brand_list[0])]
# mat_list = df_cleaned_select['Material'].unique()
#
# out_put = post_processing_and_analysis.get_list(matchings_pkl=matchings_pkl, df_cleaned=df_cleaned,
#                                                 material_id=mat_list[2])
#
# headerColor = 'grey'
# rowEvenColor = 'lightgrey'
# rowOddColor = 'white'
#
# fig = ff.create_table(out_put[['Material', 'Material Desc(CM)']])

controls, fig = chart_template.create_dyn_list(data=df_cleaned,
                                               matches=matchings_pkl,
                                               filter_col='Material',
                                               # filter_lab_col='Material Desc(CM)',
                                               filter_col2='Brand',
                                               filter_col3='Grouping'
                                               )

test = dcc.Markdown('''
* ...
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Matching list",
                                          left_panel_content=fig,
                                          right_panel_content=controls
                                          )
