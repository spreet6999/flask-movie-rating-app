# -*- coding: utf-8 -*-
# import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from random import random
import logging
# import pandas as pd
# import plotly.plotly as py
# from plotly import graph_objs as go
# import math
from app import app, project_name, logo, app_prefix, host, app_port
# from apps import dynamic_test
from tabs import tab_1_exec_sum_portfolio, tab_2_overview
    # tab_2_5_portfolio_performance, \
    # tab_4_part_lists, tab_5_dynamic_tree_plot, tab_6_dynamic_bar_plot, tab_6_bom_heatmap, tab_8_bom_table, \
    # tab_7_sample_table

# tab_5_t_sne_scatter_plot, tab_6_explore_topic_plot, tab_7_topic_word_importance_plot, tab_8_optimal_num_topics_plot

# This is contains the layout for the application, in this example there is a single container for all of the tabs
# the content of the tabs is generated dynamically depending on what tab is clicked
spin_id_name = 'spinner_' + str(round(random() * 10 ** 6))

try:
    portfolio_layout = html.Div([
        # This is the overall header for the page - you can modify the logo name and content from tha app.py file
        # other properties like background color can be set in the CSS file which is in the assets folder

        # Here is the container for all of the tabs. To create a new tab or page you have to copy onr of the children below
        # and set the layout in the dynamic_test.py file to point to an html layout for the page as well as add content
        # to set the style modify the CSS file in the assets folder
        dcc.Tabs(
            id="ut-tabs-with-classes",
            value='tab-2',
            parent_className='custom-tabs',
            className='custom-tabs-container',
            children=[
                dcc.Tab(
                    label='Overview',
                    value='tab-1',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                # dcc.Tab(
                #     label='Portfolio performance overview',
                #     value='tab-2-5',
                #     className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                dcc.Tab(
                    label='Pareto charts',
                    value='tab-2',
                    className='custom-tab',
                    selected_className='custom-tab--selected'
                ),
                # dcc.Tab(
                #     label='Complexity tree',
                #     value='tab-5', className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                # dcc.Tab(
                #     label='Attribute Impact',
                #     value='tab-6',
                #     className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                # dcc.Tab(
                #     label='List of SKUs',
                #     value='tab-4',
                #     className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                # dcc.Tab(
                #     label='BOM Heatmap view',
                #     value='tab-7',
                #     className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                # dcc.Tab(
                #     label='Compare BOMs',
                #     value='tab-8',
                #     className='custom-tab',
                #     selected_className='custom-tab--selected'
                # ),
                # dcc.Tab(
                #     label='Table Explorer',
                #     value='tab-9',
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
        html.Div(id='ut-tabs-content-classes', className="row", style={"margin": "0.5% 1.8%"}),
    ])    
except Exception as e:
    logging.error(f'Exception while building `portfolio_layout`: {e}', exc_info=True)
    raise e

# This callback is used to dynamically get the content for each of the tabs
@app.callback(Output('ut-tabs-content-classes', 'children'),
              [Input('ut-tabs-with-classes', 'value')])
def render_content(tab):
    # the dyn_content function in the dynamic_test file is currently used to generate content given a tab ID.
    # return dynamic_test.dyn_content(page_num=tab)
    # The structure below can be used to dynamically get content from each of the tabs
    try:
        # if tab == 'tab-1':
        #     logging.info(f"Tab: Overview")
        #     return tab_1_exec_sum_portfolio.layout
        # elif tab == 'tab-2':
        #     logging.info(f"Tab: Pareto charts")
        #     logging.info(f"Tab: CHECKPOINT 2")
        #     return tab_2_overview.layout
        if tab == 'tab-2':
            logging.info(f"Tab: Pareto charts")
            logging.info(f"Tab: CHECKPOINT 2")
            return tab_2_overview.layout
        # elif tab == 'tab-2-5':
        #     logging.info(f"Tab: Portfolio performance overview")
        #     return tab_2_5_portfolio_performance.layout
        # elif tab == 'tab-4':
        #     logging.info(f"Tab: List of SKUs")
        #     return tab_4_part_lists.layout
        # elif tab == 'tab-5':
        #     logging.info(f"Tab: Complexity Tree")
        #     return tab_5_dynamic_tree_plot.layout
        # elif tab == 'tab-6':
        #     logging.info(f"Tab: Attribute Impact")
        #     return tab_6_dynamic_bar_plot.layout
        # elif tab == 'tab-7':
        #     logging.info(f"Tab: BOM Heatmap")
        #     return tab_6_bom_heatmap.layout
        # elif tab == 'tab-8':
        #     logging.info(f"Tab: Compare BOMs")
        #     return tab_8_bom_table.layout
        # elif tab == 'tab-9':
        #     logging.info(f"Tab: Table Explorer")
        #     return tab_7_sample_table.layout
        else:
            return tab_1_exec_sum_portfolio.layout
    except Exception as e:
        logging.error(f'Exception while `render_content` for tab: {tab}: {e}', exc_info=True)
        raise e
