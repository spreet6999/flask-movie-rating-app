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
                                                        content=html.Ul([
                                                            html.Li(children=[html.B('Overview:'),
                                                                              'The following notebook showcases the structured sensor data pipeline, with vizualizations from two components of the pipeline']),
                                                            html.Ul([
                                                                html.Li('EDA/Sensor Data Cleanup'),
                                                                html.Li('Model Performance')
                                                            ]),
                                                            html.Li(children=[html.B('EDA/Sensor Data Cleanup: '),
                                                                              'The following are illustrated utilizing the raw input data']),
                                                            html.Ul([
                                                                html.Li('Relationship between sensor variables and outcome variable'),
                                                                html.Li('Timeseries plot between sensor variables and outcome variable'),
                                                                html.Li('Boxplot of outliers'),
                                                                html.Li('Summary of missing sensor data'),
                                                                html.Li('Correlation matrix between sensors')
                                                            ]),
                                                            html.Li(children=[html.B('Model performance: '),
                                                                              'Commonly used diagrams and metrics for evaluating binary classification']),
                                                            html.Ul([
                                                                html.Li('ROC Curve'),
                                                                html.Li('Precision-Recall Curve')                                                            ])
                                                        ])
                                                    ),
                                                    )
