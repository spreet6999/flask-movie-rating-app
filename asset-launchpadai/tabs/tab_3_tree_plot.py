import pandas as pd
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import app, df_cleaned  # other objects such as "indicator" can be imported and used it

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

df = df_cleaned[df_cleaned['Grouping'] == 'SAW']
df = df[(df['Gbl Prev 12Mo GSV $'] > 0) & (df['Gbl Prev 12Mo Qty'] > 0)]

levels = ['reg_list', 'Brand', 'Segment 4', 'Segment 3',
          'Segment 2', 'Segment 1']  # levels used for the hierarchical chart, first value is outer most ring
color_columns = ['Gbl Prev 12Mo GSV $', 'Gbl Prev 12Mo Margin ($)']
value_column = 'Material_base'
value_name = 'Count of base SKUs'

figure = chart_template.dynamic_pie_chart(title="Complexity tree:", data=df, levels=levels, color_columns=color_columns,
                                          value_column=value_column, value_type="count", value_name=value_name)

layout = page_template.layout_right_small(page_lead="Complexity Tree",
                                          left_panel_content=template_obj.graph_content(
                                              figure=figure),
                                          right_panel_content=template_obj.title_textbox(title="Key points:",
                                                                                         content=right_content)
                                          )
