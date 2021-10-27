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
from app import df_bom  # other objects such as "indicator" can be imported and used it
import numpy as np
from src.portfolio_ai.nodes import post_processing_and_analysis

# main code to build the figures and controls goes here -----------------------------------------------------------
# level_list = ['Segment 1', 'Segment 2', 'Segment 3', 'Segment 4', 'Segment 5', 'Segment 6', 'Segment 7', 'Segment 8',8
#               'Segment 9', 'Segment 10', 'Brand', 'reg_list', 'Material_base', 'Grouping', 'Category', 'Portfolio']

# function to build the graph and control content
controls, fig = chart_template.create_bom_heatmap_plot(data=df_bom,
                                                       filter_col='Material_base',
                                                       filter_col_2='Segment 1',
                                                       filter_col_3='Grouping',
                                                       filter_col_4='Brand',
                                                       filter_col_5='Region'
                                                       # level_list=level_list
                                                       )


# put the figures into a page layout -------------------------------------------------------------------------------

# put everything into the layout
layout = page_template.layout_right_small(page_lead="BOM heatmap:",
                                          left_panel_content=fig,
                                          right_panel_content=controls
                                          )
