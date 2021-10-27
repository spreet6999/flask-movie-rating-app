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
from pages import tab_1_exec_sum, tab_2_test_plot, tab_3_word_frequency_plot, tab_4_topic_dist_plot, \
    tab_5_t_sne_scatter_plot, tab_6_explore_topic_plot, tab_7_topic_word_importance_plot


# This is contains the layout for the application, in this example there is a single container for all of the tabs
# the content of the tabs is generated dynamically depending on what tab is clicked

unstructured_text_layout = html.Div([
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
                value='tab-1',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Word Count Distribution',
                value='tab-2',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Word Frequency Chart',
                value='tab-3', className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Topic Distributions',
                value='tab-4',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Clustering T-SNE Plot',
                value='tab-5',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Data Explore',
                value='tab-6',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            dcc.Tab(
                label='Topic Word Importance',
                value='tab-7',
                className='custom-tab',
                selected_className='custom-tab--selected'
            ),
            # dcc.Tab(
            #     label='Tab eight',
            #     value='tab-8',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
            # dcc.Tab(
            #     label='Tab nine',
            #     value='tab-9',
            #     className='custom-tab',
            #     selected_className='custom-tab--selected'
            # ),
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
    if tab == 'tab-1':
        return tab_1_exec_sum.layout
    elif tab == 'tab-2':
        return tab_2_test_plot.layout
    elif tab == 'tab-3':
        return tab_3_word_frequency_plot.layout
    elif tab == 'tab-4':
        return tab_4_topic_dist_plot.layout
    elif tab == 'tab-5':
        return tab_5_t_sne_scatter_plot.layout
    elif tab == 'tab-6':
        return tab_6_explore_topic_plot.layout
    elif tab == 'tab-7':
        return tab_7_topic_word_importance_plot.layout
    # elif tab == 'tab-8':
    #     return tab_8_sample_two_panel.layout
#     elif tab == 'tab-9':
#         return tab_9_dyn_analysis_x.layout
