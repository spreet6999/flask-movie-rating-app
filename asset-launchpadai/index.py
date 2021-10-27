# -*- coding: utf-8 -*-
# import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
# import pandas as pd
# import plotly.plotly as py
# from plotly import graph_objs as go
# import math
import logging
from app import app, project_name, logo, app_prefix, host, app_port
# from apps import dynamic_test

from pages import portfolio #, unstructured_text, sensor, syslog


# This is contains the layout for the application, in this example there is a single container for all of the tabs
# the content of the tabs is generated dynamically depending on what tab is clicked
try:
    app.layout = html.Div([
        html.Div([

            html.A(href="/app/", children=[html.Span(project_name, className='app-title')]),
            
            html.Div(
                html.Img(
                    src=app.get_asset_url(logo),
                    height="100%"),
                style={"float": "right", "height": "100%"})
        ],
            className="row header"
        ),

        dcc.Location(id='url', refresh=False),
        html.Div(portfolio.portfolio_layout, id='page-content')
    ])
except Exception as e:
    logging.error(f'Exception while building `app.layout`: {e}', exc_info=True)
    raise e


url_input = Input('url', 'pathname')
# logging.info(f'HELLO WORLD')
# logging.info(f'HELLO WORLD')
# logging.info(f'url_input: {url_input}')

# Update the index
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])
# def display_page():
#     # if pathname == '/app/unstructured_text':
#     #     return unstructured_text.unstructured_text_layout
#     # elif pathname == '/app/sensor':
#     #     return sensor.sensor_layout
#     # elif pathname == '/app/unstructured_syslog_text':
#     #     return syslog.syslog_layout
#     # else:
#     # print(pathname)
#     return landing.landing_page_layout


def main():
    logging.info(f"Starting server on host: ME {host} and port: {app_port}")
    logging.info(f"Checkpoint 1")
    app.run_server(debug=False, host=host, port=app_port)


# This starts the application - when running the application have fo all this app.run_server function, it will not work
# to run from any other files in the folder
if __name__ == '__main__':
    logging.info(f"Starting server on host: ME2 {host} and port: {app_port}")
    logging.info(f"Checkpoint 2")
    app.run_server(debug=False, host=host, port=app_port)