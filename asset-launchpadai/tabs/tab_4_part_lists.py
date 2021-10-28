# start with some imports--------------------------------------------------------------------------------------------
# import pandas as pd
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
from app import df_cleaned  # other objects such as "indicator" can be imported and used it
import numpy as np
from src.portfolio_ai.nodes import post_processing_and_analysis

# main code to build the figures and controls goes here -----------------------------------------------------------
controls, fig = chart_template.create_dyn_sku_list(data=df_cleaned,
                                                   filter_col='Portfolio',
                                                   filter_col_2='Category',
                                                   filter_col_3='Brand',
                                                   filter_col_4='SubSBU',
                                                   filter_col_5='SBU',
                                                   filter_col_6='Region',
                                                   )

# put the figures into a page layout -------------------------------------------------------------------------------

# put everything into the layout
layout = page_template.layout_right_small(page_lead="SKU list",
                                          left_panel_content=fig,
                                          right_panel_content=controls
                                          )