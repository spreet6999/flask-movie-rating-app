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

right_content = template_obj.blank_textbox(
    content=html.Ul([
        html.Li(children=[html.B('First major point: '),
                          'description of first major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point'),
            html.Li('Third minor point')
        ]),
        html.Li(children=[html.B('Second major point: '),
                          'description of second major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point')
        ]),
        html.Li(children=[html.B('Third major point: '),
                          'description of third major']),
        html.Li(children=[html.B('Fourth major point: '),
                          'description of fourth major']),
        html.Ul([
            html.Li('First minor point'),
            html.Li('Second minor point'),
            html.Li('Third minor point')
        ]),
        html.Li(children=[html.B('Fifth major point'),
                          'description of fifth major'])
    ])
)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
# print(df.head())

levels = ['salesperson', 'county', 'region']  # levels used for the hierarchical chart
color_columns = ['sales', 'calls']
value_column = 'calls'
impact_col = 'sales'

figure = chart_template.dynamic_pie_chart(data=df, levels=levels, color_columns=color_columns,
                                          value_column=value_column, impact_col=impact_col)

layout = page_template.layout_two_panel(page_lead="Test page lead",
                                        left_panel_content=template_obj.graph_content(
                                            figure=figure),
                                        right_panel_content=template_obj.title_textbox(title="Key points;",
                                                                                       content=right_content)
                                        )
