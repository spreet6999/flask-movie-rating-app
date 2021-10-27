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
from tabs import utmcc_exec_sum_syslog, utmcc_label_count, utmcc_select_classifier_model \
, utmcc_confusion_matrix

syslog_layout = html.Div([
    # This is the overall header for the page - you can modify the logo name and content from tha app.py file
    # other properties like background color can be set in the CSS file which is in the assets folder

    # Here is the container for all of the tabs. To create a new tab or page you have to copy onr of the children below
    # and set the layout in the dynamic_test.py file to point to an html layout for the page as well as add content
    # to set the style modify the CSS file in the assets folder
    dcc.Tabs(
        id="utmcc-tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Overview',
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Label Distribution',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Select Classifier Model',
                value='tab-3',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Confusion Matrix',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected',
                disabled = False
            ),

        ]),
    html.Div(id='utmcc-tabs-content-classes', className="row", style={"margin": "0.5% 1.8%"}),
])

# This callback is used to dynamically get the content for each of the tabs
@app.callback(Output('utmcc-tabs-content-classes', 'children'),
              [Input('utmcc-tabs-with-classes', 'value')])
def render_content(tab):
    # the dyn_content function in the dynamic_test file is currently used to generate content given a tab ID.
    # return dynamic_test.dyn_content(page_num=tab)
    # The structure below can be used to dynamically get content from each of the tabs
    if tab == 'tab-1':
        return utmcc_exec_sum_syslog.layout
    elif tab == 'tab-2':
        return utmcc_label_count.layout
    elif tab == 'tab-3':
        return utmcc_select_classifier_model.layout
    elif tab == 'tab-4':
        return utmcc_confusion_matrix.layout