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

# Here is an example of creating an executive summary in a tab. This example uses the layout_single_panel from the
# page_layout.py file. Note that the content is manually created inside the function call but could be generated
# outside the call and passed as a variable into the function. Also note to have "selected bold text" the "children"
# property of the html.Li or html.Ul is used, to create bold text put the text inside of a html.B function as below.
# The text color for the bold text is set in the CSS file in the assets folder. Finally, to crete a sublist at any
# point simply add a html.Ul function and add as many "list items" (html.Li) to that function as needed for elements
# in the sub list
layout = page_template. \
    layout_single_panel(page_lead="Overview: ",
                        main_panel_content=template_obj.blank_textbox(
                            content=html.Div([
                                html.Ul([
                                    html.Li(children=[html.B('Overall portfolio analysis:'), ""]),

                                    html.Ul([
                                        html.Li(children=[html.B('Portfolio performance overview tab: '),
                                                          '''the portfolio heath tab gives the health of portfolios by 
                                                          looking at GSV per SKU in different categories''']),
                                        html.Li(children=[html.B('Complexity tree tab: '),
                                                          '''the complexity tree tab creates a dynamic starburst chart 
                                                          to show the complexity of the portfolio and make trimming 
                                                          decisions''']),
                                        html.Li(children=[html.B('Attribute impact tab: '),
                                                          '''the attribute impact tab shows...''']),
                                        html.Li(children=[html.B('List of SKUs: '),
                                                          '''the list of SKUs tab gives a dynamic list of SKUs that can 
                                                          be filtered by several variables''']),
                                        html.Li(children=[html.B('Pareto charts tab: '),
                                                          '''the overview tabs gives pareto chart for GDM, GSV, and sku 
                                                           count broken down by different categories''']),
                                    ]),

                                    html.Li(children=[html.B('BOM comparison:'), ""]),
                                    html.Ul([
                                        html.Li(children=[html.B('BOM heatmap tab: '),
                                                          '''the BOM heatmap tab can be used to show the reuse of 
                                                          components of BOMs within the a portfolio or other groups of 
                                                          SKUs)''']),
                                        html.Li(children=[html.B('BOM comparison tab: '),
                                                          '''The BOM comparison tab can be used to explore the content 
                                                          of two materials based on their BOMs and export'''])
                                    ]),

                                    html.Li(children=[html.B('Matching tool:'), ""]),
                                    html.Ul([
                                        html.Li(children=[html.B('SKU matching tool tab: '),
                                                          '''the SKU matching tool is a tool to look up the closest 
                                                          matching SKU within a portfolio, brand of category (work in 
                                                          progress)''']),
                                        html.Li(children=[html.B('Additional tabs to be added: '),
                                                          '''....'''])
                                    ]),
                                    html.I('Additional tabs to be added this page is a work in progress...')
                                ])
                            ])
                        )
                        )
