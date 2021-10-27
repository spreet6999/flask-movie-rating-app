### NOT USED


# import math

# import pandas as pd
# import quart.flask_patch
import flask
import dash
from flask import request, Flask, current_app
# import dash_core_components as dcc
import dash_html_components as html
from pathlib import Path
from kedro.context import load_context

current_dir = Path.cwd()  # this points to 'asset-launchpadai/apps' folder
proj_path = current_dir.parent  # point back to the root of the project
if not str(proj_path).endswith('troubleshooting_ai'):
    proj_path = proj_path / 'troubleshooting_ai'

context = load_context(proj_path)


host = '127.0.0.1'
app_port = 8050
app_prefix = '/sensor/'
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, routes_pathname_prefix=app_prefix)
app.config.suppress_callback_exceptions = True


# set the name for the project here and the name of the logo file, which has to be in the assets folder
logo = 'logoMcKinsey.png'
project_name = "Services.AI: Advanced Troubleshooting"
app.title = project_name



# returns top indicator div
def indicator(color, id_value, text="test",):
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