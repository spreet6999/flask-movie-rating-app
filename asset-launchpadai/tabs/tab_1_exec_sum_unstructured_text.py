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
layout = page_template.layout_single_panel(page_lead="Executive summary: ",
                                                    main_panel_content=template_obj.blank_textbox(
                                                        content=html.Div([
                                                            html.Ul([
                                                                html.Li(children=[html.B('Exploratory Data Analysis:'), ""]),

                                                                html.Ul([
                                                                    html.Li(children=[html.B('Word count distribution: ')
                                                                    , '''When working with large number of documents, its good to know how big the documents are as whole. 
                                                                    This graph helps us understand, what specific preprocessing steps needs to be taken to produce good results in topic modeling.''']),
                                                                    html.Li(children=[html.B('Word frequency plot: ')
                                                                    , '''Word frequency chart helps us understand the top words which are prevalent in the text corpus. 
                                                                    The words identified are from preprocessed text, not from the original text documents.'''])
                                                                ]),
                                                                
                                                                html.Li(children=[html.B('Topic Modeling:'), ""]),
                                                                html.Ul([
                                                                    html.Li(children=[html.B('Topic distribution: ')
                                                                    , '''Topic word distribution is helpful to understand the inherent difference in the topics based on the size of the documents.''']),
                                                                    html.Li(children=[html.B('TSNE Clustering of topics: ')
                                                                    , '''To visualize all the topics in a single chart, 
                                                                    we can use clustering techniques like T-SNE(t-distributed stochastic neighbor embedding) which work best in topic modeling.'''])
                                                                ])
                                                                ,
                                                                html.I('Work in Progress...')
                                                            ])
                                                        ])
                                                )
                                            )
                                                    
