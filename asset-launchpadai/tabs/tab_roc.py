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


import numpy as np

y_preds = context.catalog.load('y_preds')
y_test = context.catalog.load('y_test')

#calculate ROC curve
lr_fpr, lr_tpr, _ = roc_curve(y_test, y_preds)

fig = Figure()

fig.add_trace(
    Scatter(x=lr_fpr, y=lr_tpr, name="ROC Curve"),
)

#graph random guess curve
fig.add_trace(
    Scatter(x=[0, 1], y=[0, 1], name="Random Guess"),
)

fig.update_yaxes(title_text="True Positive Rate")
fig.update_xaxes(title_text="False Positive Rate")



# Add traces


# Add figure title
fig.update_layout(
    title_text="ROC Curve, AUC= %.3f" % auc(lr_fpr, lr_tpr)
)

test = dcc.Markdown('''
ROC Curve (Receiver Operating Curve)
The higher AUC (area under the curve), the better the model is at distinguishing classes, so this model performs very well 
''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="ROC",
                                          left_panel_content=template_obj.graph_content(
                                             figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
