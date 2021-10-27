# -*- coding: utf-8 -*-
# import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# import pandas as pd
# import plotly.plotly as py
# from plotly import graph_objs as go
# import math
from app import app, project_name, logo, app_prefix, host, app_port
# from apps import dynamic_test
from tabs import tab_overview, tab_sensor_data_exploration, tab_missing_data_plot, \
    tab_correlation_matrix, tab_outliers, tab_roc, tab_pr \
    # , tab_var_importance

sensor_layout = html.Div([

    # This is the overall header for the page - you can modify the logo name and content from tha app.py file
    # other properties like background color can be set in the CSS file which is in the assets folder
    # Here is the container for all of the tabs. To create a new tab or page you have to copy onr of the children below
    # and set the layout in the dynamic_test.py file to point to an html layout for the page as well as add content
    # to set the style modify the CSS file in the assets folder
    dcc.Tabs(
        id="ssd-tabs-with-classes",
        value='overview_page',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Overview',
                value='overview_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Sensor Data Exploration',
                value='sensor_data_exploration_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            # dcc.Tab(
            #     label='Sensor 49 Data Exploration',
            #     value='tab-8',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
            # dcc.Tab(
            #     label='Timescale Data Exploration',
            #     value='tab-9',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
            dcc.Tab(
                label='Missing Data',
                value='missing_data_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Correlation Matrix',
                value='correlation_matrix_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            # dcc.Tab(
            #     label='Outliers',
            #     value='tab-13',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
            dcc.Tab(
                label='ROC',
                value='roc_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Precision-Recall',
                value='precision_recall_curve_page',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            # dcc.Tab(
            #     label='Model Variable Importance',
            #     value='feature_importance_page',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
        ]),
    html.Div(id='ssd-tabs-content-classes', className="row", style={"margin": "0.5% 1.8%"}),
])


# This callback is used to dynamically get the content for each of the tabs
@app.callback(Output('ssd-tabs-content-classes', 'children'),
              [Input('ssd-tabs-with-classes', 'value')])
def render_content(tab):
    # the dyn_content function in the dynamic_test file is currently used to generate content given a tab ID.
    # return dynamic_test.dyn_content(page_num=tab)
    # The structure below can be used to dynamically get content from each of the tabs
    if tab == 'overview_page':
        return tab_overview.layout
    elif tab == 'sensor_data_exploration_page':
        return tab_sensor_data_exploration.layout
    # elif tab == 'tab-8':
    #     return tab_8_test_plot.layout
    # elif tab == 'tab-9':
    #     return tab_9_test_plot.layout
    elif tab == 'missing_data_page':
        return tab_missing_data_plot.layout
    elif tab == 'correlation_matrix_page':
        return tab_correlation_matrix.layout
    # elif tab == 'tab-13':
    #     return tab_13_outliers.layout
    elif tab == 'roc_page':
        return tab_roc.layout
    elif tab == 'precision_recall_curve_page':
        return tab_pr.layout
    # elif tab == 'feature_importance_page':
    #     return tab_var_importance.layout
