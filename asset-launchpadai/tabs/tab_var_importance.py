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
from sklearn.metrics import precision_score, recall_score, accuracy_score, roc_curve, auc, precision_recall_curve, f1_score 
from xgboost import plot_importance
import pickle


import numpy as np

model = context.catalog.load('model_output')

xgb_model_loaded = pickle.loads(model)


# This works only with XGBoost models
#get the list of feature names
#and the feature importances
#and graph

x = xgb_model_loaded.get_booster().feature_names


y = xgb_model_loaded.feature_importances_

fig = Figure([Bar(x=x, y=y)])
fig.update_layout(title_text='Feature Importance')


test = dcc.Markdown('''
Feature Importance
- Sensor 00 shows the highest importance
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Feature Importance",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
