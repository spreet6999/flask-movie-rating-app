# -*- coding: utf-8 -*-
# import json
# import math

import pandas as pd
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
#import plotly.plotly as py
import plotly.express as px
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import app  # other objects such as "indicator" can be imported and used it

# data that is used in the the dynamic plot
df = px.data.gapminder()
# 'country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap', 'iso_alpha', 'iso_num'
x_cols = ['country', 'continent', 'year', 'iso_alpha', 'iso_num']
x_cols_value = 'country'
y_cols = ['lifeExp', 'pop', 'gdpPercap']
y_cols_val = 'pop'
text_cols = ['lifeExp', 'pop', 'gdpPercap']
text_cols_val = 'pop'
text_vals = 'pop'
filter_cols = ['year', 'continent', 'country']
filter_vals = [None, None, None]
data_set = df
data_set = data_set[data_set[filter_cols[0]] == filter_vals[0]]
data_set = data_set[data_set[filter_cols[1]] == filter_vals[1]]
fig = px.bar(data_set, y=y_cols_val, x=x_cols_value, text=text_vals)
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
figure_1 = fig

# slider_filter_html = None

# build the controls panel

filter_title_html = None
filter_control_title = "Select filter value: "
control_title = "Plot controls: "
control_title_html = None if filter_cols[0] is None else html.Div(control_title,
                                                                  style={"color": "var(--Bold-text)",
                                                                         "text-align": "left",
                                                                         "font weight": "1200"})

index = 0
content_test = [control_title_html]
filter_ids = []
for filter_col in filter_cols:
    filter_id = 'filter-id-' + str(index)
    filter_title_html = html.Div(filter_control_title + filter_col, style={"color": "var(--Bold-text)",
                                                                           "text-align": "left",
                                                                           "font weight": "800"})
    drop_down_filter_html = html.Div([
        dcc.Dropdown(
            id=filter_id,
            value=filter_vals[index]
        )
    ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
    content_test.append(filter_title_html)
    content_test.append(drop_down_filter_html)
    filter_ids.append(filter_id)
    index += 1
jj = 0
for filter_id_out in filter_ids:
    controls = html.Div(content_test)
    input_var = []
    filter_ids_pos = []
    filter_col_call_back = []
    filter_vals_pos = []
    var_position = 0
    output_var = Output(filter_id_out, 'options')
    i = 0
    for filter_id in filter_ids:
        if filter_id != filter_id_out:
            input_var.append(Input(filter_id, 'value'))
            filter_ids_pos.append(i)
            filter_col_call_back.append(filter_cols[i])
            filter_vals_pos.append(var_position)
            var_position += 1
        i += 1

    col_select = filter_cols[jj]
    jj += 1
    # print(filter_col_call_back)
    # print(filter_ids_pos)
    # print(input_var)
    # print(output_var)

    @app.callback(output_var, input_var)
    def update_filter(var_1=None, var_2=None, var_3=None, var_4=None, var_5=None, var_6=None, var_7=None, var_8=None,
                      var_9=None, var_10=None):
        # put the vars in a list to select using position variable just created
        dyn_vars = [var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10]
        ii = 0
        dff = df
        for col in filter_col_call_back:
            value = dyn_vars[filter_vals_pos[ii]]
            if value is not None:
                # print(value)
                # print(col)
                dff = dff[dff[col] == value]
            ii += 1

        # print(ii)
        # filter_vars =
        # dynamically set the variables based on position variable previously defined
        print(col_select)
        print(filter_id_out)
        return [{'label': j, 'value': j} for j in dff[col_select].unique()]

# put everything into the layout
layout = page_template.layout_right_small(page_lead="Test page lead",
                                          left_panel_content=template_obj.graph_content(figure=figure_1),
                                          right_panel_content=controls,
                                          )
