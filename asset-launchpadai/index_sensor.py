### NOT USED

# -*- coding: utf-8 -*-
# import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# import pandas as pd
# import plotly.plotly as py
# from plotly import graph_objs as go
# import math
from app_sensor import app, project_name, logo, app_prefix, host, app_port
# from apps import dynamic_test
from pages import tab_1a_exec_sum, tab_7_test_plot, tab_8_test_plot, \
    tab_9_test_plot, tab_11_missing_data_plot, tab_12_correlation_matrix,\
    tab_13_outliers, tab_14_roc, tab_15_pr
    #     , tab_9_dyn_analysis_x

# This is contains the layout for the application, in this example there is a single container for all of the tabs
# the content of the tabs is generated dynamically depending on what tab is clicked
app.layout = html.Div([

    # This is the overall header for the page - you can modify the logo name and content from tha app.py file
    # other properties like background color can be set in the CSS file which is in the assets folder
    html.Div([

        html.Span(project_name, className='app-title'),

        html.Div(
            html.Img(
                src=app.get_asset_url(logo),
                height="100%"),
            style={"float": "right", "height": "100%"})
    ],
        className="row header"
    ),
    # Here is the container for all of the tabs. To create a new tab or page you have to copy onr of the children below
    # and set the layout in the dynamic_test.py file to point to an html layout for the page as well as add content
    # to set the style modify the CSS file in the assets folder
    dcc.Tabs(
        id="tabs-with-classes",
        value='tab-1',
        parent_className='custom-tabs',
        className='custom-tabs-container',
        children=[
            dcc.Tab(
                label='Overview',
                value='tab-1a',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Sensor Data Exploration',
                value='tab-7',
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
                value='tab-11',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Correlation Matrix',
                value='tab-12',
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
                value='tab-14',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Precision-Recall',
                value='tab-15',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
        ]),
    html.Div(id='tabs-content-classes', className="row", style={"margin": "0.5% 1.8%"}),
])


# This callback is used to dynamically get the content for each of the tabs
@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs-with-classes', 'value')])
def render_content(tab):
    # the dyn_content function in the dynamic_test file is currently used to generate content given a tab ID.
    # return dynamic_test.dyn_content(page_num=tab)
    # The structure below can be used to dynamically get content from each of the tabs
    if tab == 'tab-1a':
        return tab_1a_exec_sum.layout
    elif tab == 'tab-7':
        return tab_7_test_plot.layout
    # elif tab == 'tab-8':
    #     return tab_8_test_plot.layout
    # elif tab == 'tab-9':
    #     return tab_9_test_plot.layout
    elif tab == 'tab-11':
        return tab_11_missing_data_plot.layout
    elif tab == 'tab-12':
        return tab_12_correlation_matrix.layout
    # elif tab == 'tab-13':
    #     return tab_13_outliers.layout
    elif tab == 'tab-14':
        return tab_14_roc.layout
    elif tab == 'tab-15':
        return tab_15_pr.layout


#     elif tab == 'tab-9':
#         return tab_9_dyn_analysis_x.layout


def main():
    app.run_server(debug=False, host=host, port=app_port)


# This starts the application - when running the application have fo all this app.run_server function, it will not work
# to run from any other files in the folder
if __name__ == '__main__':
    app.run_server(debug=True, host=host, port=app_port)