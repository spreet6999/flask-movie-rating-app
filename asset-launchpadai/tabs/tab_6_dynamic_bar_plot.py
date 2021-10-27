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
level_list = ['Segment 1', 'Segment 2', 'Segment 3', 'Segment 4', 'Segment 5', 'Segment 6', 'Segment 7', 'Segment 8',
              'Segment 9', 'Segment 10', 'Brand', 'reg_list', 'Material_base', 'Grouping', 'Category', 'Portfolio']

# read from db instead of flat files
# WAY 1
# df_cleaned = read_from_db()
controls, fig = chart_template.create_dyn_bar_chart(data=df_cleaned,
                                                    filter_col_1='Segment 2',
                                                    filter_col_2='Segment 1',
                                                    filter_col_3='Grouping',
                                                    filter_col_4='SubSBU',
                                                    filter_col_5='SBU',
                                                    filter_col_6='Region',
                                                    level_list=level_list
                                                    )
# WAY 2
# df_cleaned = read_from_db_filtered_data()
# controls, fig = chart_template.create_dyn_bar_chart(data=df_cleaned,
#                                                     filter_col_1='Segment 2',
#                                                     filter_col_2='Segment 1',
#                                                     filter_col_3='Grouping',
#                                                     filter_col_4='SubSBU',
#                                                     filter_col_5='SBU',
#                                                     filter_col_6='Region',
#                                                     level_list=level_list
#                                                     )

# put the figures into a page layout -------------------------------------------------------------------------------

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Attribute impact",
                                          left_panel_content=fig,
                                          right_panel_content=controls
                                          )
