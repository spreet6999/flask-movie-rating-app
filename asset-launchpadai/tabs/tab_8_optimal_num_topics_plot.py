# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
import numpy as np
from random import random
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
import plotly.express as px
from apps import template_obj, chart_template, page_template
from app import app, context  # other objects such as "indicator" can be imported and used it
from collections import Counter

gensim_coherence_values = context.catalog.load('gensim_coherence_values')

coherence_values = pd.Series(gensim_coherence_values).to_frame()
coherence_values.reset_index(inplace = True)
coherence_values.columns = ['topics', 'coherence_values']

fig = px.line(coherence_values, x="topics", y="coherence_values")
fig.update_layout(
    title="Optimal Number of Topics",
    xaxis_title="Number of Topics",
    yaxis_title="Coherence Score")



test = dcc.Markdown('''

''')

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Topic Clustering T-SNE plot:",
                                          left_panel_content=template_obj.graph_content(
                                              figure=fig),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=test)
                                          )
