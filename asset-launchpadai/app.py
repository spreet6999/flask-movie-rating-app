# import math

import logging
import time
import pandas as pd
import numpy as np
# import quart.flask_patch
import flask
import dash
from flask import request, Flask, current_app
# import dash_core_components as dcc
import dash_html_components as html
from pathlib import Path
# from kedro.framework.context import load_context

current_dir = Path.cwd()  # this points to 'asset-launchpadai/apps' folder
proj_path = current_dir.parent  # point back to the root of the project
# print(f"current_dir -> {current_dir}")
# print(f"proj_path -> {proj_path}")
if not str(proj_path).endswith('portfolio_ai'):
    proj_path = proj_path / 'portfolio_ai'

# context = load_context(proj_path)

host = '0.0.0.0'
app_port = 8050
app_prefix = '/app/'
app_pathname_prefix = '/user/jupyter/proxy/8050' + app_prefix
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, routes_pathname_prefix=app_prefix)
app.config.suppress_callback_exceptions = True

# set the name for the project here and the name of the logo file, which has to be in the assets folder
logo = 'Stanley_Black__Decker_logo.png'
project_name = "Portfolio.AI: Complexity Analysis"
app.title = project_name

# ! COMMENT ALL DATA LOAD STATEMENTS
# ! DATA WILL COME FROM DB via an API
# load all of the data
# matchings_pkl = context.catalog.load('top_candidates_by_sku_dict')
# start_time = time.time()
# df_cleaned = context.catalog.load('master_dataframe_cln')
# end_time = time.time()
# logging.info(f'df_cleaned read in {end_time-start_time}')
# start_time = time.time()
# df_cleaned.loc[df_cleaned['SalesThreshold'] == 0, 'SalesThreshold'] = 1
# df_cleaned.loc[df_cleaned['SalesThreshold'].isnull(), 'SalesThreshold'] = 1
# df_cleaned['reg_list'] = df_cleaned['reg_list'].replace("_NA", "")
# df_cleaned['reg_list'] = df_cleaned['reg_list'].replace("NA_", "")
# df_cleaned = df_cleaned.applymap(lambda s: s.upper().strip() if type(s) == str else s)
# end_time = time.time()
# print("TRYING TO SAVE DF_CLEANED_SAMPLE.CSV")
# df_cleaned.head(50).to_csv("df_cleaned_sample.csv")
# print("DONE TRYING TO SAVE DF_CLEANED_SAMPLE.CSV")
# logging.info(f'df_cleaned processed in {end_time-start_time}')
# logging.info(f'type df_cleaned {type(df_cleaned)}')
# logging.info(f'df_cleaned shape {df_cleaned.shape}')
# start_time = time.time()
# df_bom = context.catalog.load('bom_details_selected')
# end_time = time.time()
# logging.info(f'df_bom read in {end_time-start_time}')
# start_time = time.time()
# df_bom = df_bom.applymap(lambda s: s.upper().strip() if type(s) == str else s)
# end_time = time.time()
# logging.info(f'df_bom processed of {end_time-start_time}')
# logging.info(f'df_bom shape {df_bom.shape}')


# material_id_list = context.params.get('sample_list')
# sample_list_file_name = context.params.get('sample_list_file_name')
# portfolio_list = context.params.get('portfolio_list')
# segment_col = context.params.get('segment_col')
# df_cleaned = df_cleaned[df_cleaned[segment_col].isin(portfolio_list)]


# returns top indicator div
def indicator(color, id_value, text="test", ):
    return html.Div(
        [

            html.P(
                text,
                className="twelve columns indicator_text"
            ),
            html.P(
                id=id_value,
                className="indicator_value"
            ),
        ],
        className="four columns indicator",

    )


def shutdown_server():
    shutdown_app = request.environ.get('werkzeug.server.shutdown')
    if shutdown_app is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    else:
        shutdown_app()
        return "server is shutting down"


@app.server.route(app_prefix + 'shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
