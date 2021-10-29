# import needed packages ----------------------------------------------------------------------------------------------
import logging
import time

from flask.globals import request
import numpy as np
import pandas as pd
import re
from random import random
import plotly.figure_factory as ff
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
from dash.dependencies import Input, Output, State  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from plotly import graph_objs as go
from app import app  # other objects such as "indicator" can be imported and used it
from apps import template, template_obj
from src.portfolio_ai.nodes import post_processing_and_analysis
import json
import requests
from queryDataFromDb.queryDataFromDb import get_pareto_chart_filter_values, get_pareto_chart_data_from_db

# api_base_url = "https://1a23-112-133-244-168.ngrok.io"
# ! User host.docker.internal instead of localhost
api_base_url = "http://host.docker.internal:9999"

  
# #Create and configure logger
# logging.basicConfig(filename="newfile.log",filemode='w')
  
# #Creating an object
# logger=logging.getLogger()
  
# #Test messages
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")

# set some global variables -------------------------------------------------------------------------------------------
# set the theme from template
# plotly_template = pio.templates["plotly_white"]
pio.templates.default = "plotly_white+mck_new"

# Define color schemes used throughout
White = '#FFFFFF'
Black = '#000000'
Dark_Gray = '#4D4D4D'
Mid_Gray = '#7F7F7F'
Light_Gray = '#B3B3B3'
Super_Light_Gray = '#D0D0D0'
Pale_Gray = '#E6E6E6'
Deep_Blue = '#051C2C'
Cyan = '#00A9F4'
Electric_Blue = '#1F40E6'
Pale_Blue = '#AAE6F0'
Turquoise = '#3C96B4'
Pale_Electric_Blue = '#AFC3FF'
Purple = '#8C5AC8'
Pink = '#E6A0C8'
Red = '#E5546C'
Orange = '#FAA082'
Maroon = '#800000'

# create a waterfall chart with multiple subplots
def waterfall_chart_multi_col(df, level_input_select_1=None, value_cols=None,
                              orientation_mode='v', level_1=0.9, level_2=0.8):
    """ this function creates a waterfall plot with three subplots """
    temp = df
    plot_title = []
    hover_title = []
    for value_col in value_cols:
        if value_col == "Material":
            value_col_name = 'SKU count'
        elif value_col == "Gbl Prev 12Mo Margin ($)":
            value_col_name = 'GSM ($)'
        elif value_col == "Gbl Prev 12Mo GSV $":
            value_col_name = 'GSV ($)'
        else:
            value_col_name = value_col
        plot_title.append("Total: " + value_col_name)
        hover_title.append(value_col_name)

    x_value_col = level_input_select_1

    fig = make_subplots(
        cols=3, rows=1, shared_yaxes=True,
        column_widths=[0.33, 0.33, 0.33],
        subplot_titles=plot_title
    )

    col_idx = 1
    height_calc = 500
    for value_col in value_cols:
        title_idx = col_idx - 1
        val_col_cum_sum_1 = value_cols[title_idx] + '_cum_sum'  # this is the cumulative sum column
        val_col_color = 'all_color'  # this is the color column
        val_col_percent_sum_1 = value_cols[0] + '_percent_sum'  # getting this only for the left most column

        # build the values for the chart
        x_val = pd.Series(temp[x_value_col].to_list() + ['Total'])
        percent_val = pd.Series(temp[val_col_percent_sum_1].to_list() + [1])
        in_values = temp[value_col].to_list() + ['e']
        base_values = pd.Series(temp[val_col_cum_sum_1].to_list() + [temp[value_col].sum()])
        color_list = temp[val_col_color].to_list() + [Dark_Gray]
        y_val = [None if x == 'total' or x == 'Total' or x == 'tot' or x == 'tot' or x == 'e' or x == 'all'
                 else x for x in in_values]
        y_val = pd.Series(y_val)

        # get the level values to set shading
        x_val_level_1 = x_val[percent_val.gt(level_1)]
        x_val_level_1 = x_val_level_1.iloc[0]
        x_val_level_2 = x_val[percent_val.gt(level_2)]
        x_val_level_2 = x_val_level_2.iloc[0]

        # create the base values
        base_values = pd.Series(base_values)
        y_val[y_val.isnull()] = base_values[y_val.isnull()]
        y_val_base = (base_values - y_val).to_list()
        y_val = y_val.to_list()
        x_val = x_val.to_list()
        x_val_base = x_val

        if orientation_mode == 'h':
            temp_x = x_val
            temp_y = y_val
            y_val = temp_x
            x_val = temp_y
            temp_x = x_val_base
            temp_y = y_val_base
            y_val_base = temp_x
            x_val_base = temp_y

        idx = 0
        custom_data = ''
        for title in hover_title:
            # val_col_cum_sum = value_cols[idx] + '_cum_sum'  # this is the cumulative sum column if needed
            val_col_cum_sum_format = value_cols[idx] + '_cum_sum_format'
            val_col_percent_sum = value_cols[idx] + '_percent_sum'
            val_col_percent = value_cols[idx] + '_percent'
            val_col_format = value_cols[idx] + '_format'
            custom_data += '<br><br><b>' + title + ': </b>' + temp[val_col_format] + \
                           ' (' + temp[val_col_percent].map('{:,.2%}'.format) + ')<br>' + \
                           '<b>Cumulative ' + title + ': </b>' + temp[val_col_cum_sum_format] + \
                           ' (' + temp[val_col_percent_sum].map('{:,.0%}'.format) + ')'
            idx += 1

        fig.add_trace(go.Bar(
            name="",
            orientation=orientation_mode,
            x=x_val_base,
            y=y_val_base,
            marker=dict(
                color='rgba(0,0,0, 0.0)',
                line=dict(
                    color='rgba(0,0,0, 0.0)',
                    width=0
                ),
            ),
            hoverinfo='skip'
        ), 1, col_idx)

        fig.add_trace(go.Bar(
            name="",
            orientation=orientation_mode,
            x=x_val,
            y=y_val,
            marker=dict(
                color=color_list,
                line=dict(
                    color='rgba(0,0,0, 0.0)',
                    width=0
                ),
            ),
            customdata=custom_data,
            hovertemplate='<b>%{y}</b>%{customdata}',
        ), 1, col_idx)

        max_x = max(x_val)
        # this shape shades the area between 90% + of total
        fig.add_shape(
            # rectangle
            type="rect",
            x0=0,
            y0=x_val_level_1,
            x1=max_x,
            y1="Total",
            fillcolor="LightSalmon",
            opacity=0.5,
            layer="below",
            line_width=0,
            xref="x" + str(col_idx),
            yref="y" + str(col_idx),
        )
        fig.add_trace(
            go.Scatter(
                x=[max_x * 0.2],
                y=[x_val_level_1],
                text=[str(level_1*100) + '% of total'],
                showlegend=False,
                mode="text",
            ),
            row=1,
            col=col_idx,
        )
        # this shape shades the area between 80% and 90% of total
        fig.add_shape(
            # rectangle
            type="rect",
            x0=0,
            y0=x_val_level_2,
            x1=max_x,
            y1=x_val_level_1,
            fillcolor="khaki",
            opacity=0.5,
            layer="below",
            line_width=0,
            xref="x" + str(col_idx),
            yref="y" + str(col_idx),
        )
        fig.add_trace(
            go.Scatter(
                x=[max_x * 0.2],
                y=[x_val_level_2],
                text=[str(level_2 * 100) + '% of total'],
                showlegend=False,
                mode="text",
            ),
            row=1,
            col=col_idx,
        )
        if col_idx == 1:
            # add a legend for the color
            spacing = 0.015
            set_width = 120
            set_x_pos = 0.98
            fig.add_annotation(
                x=set_x_pos,
                y=1-0*spacing,
                xref="paper",
                yref="paper",
                text="GSV 2x > Complexity",
                showarrow=False,
                font=dict(
                    size=12,
                    color="#ffffff"
                ),
                align="left",
                bordercolor="#c7c7c7",
                borderwidth=0,
                borderpad=4,
                bgcolor='Green',
                width=set_width,
                opacity=0.8
            )
            fig.add_annotation(
                x=set_x_pos,
                y=1-1*spacing,
                xref="paper",
                yref="paper",
                text="GSV > Complexity",
                showarrow=False,
                font=dict(
                    size=12,
                    color="#000000"
                ),
                align="left",
                bordercolor="#c7c7c7",
                borderwidth=0,
                borderpad=4,
                bgcolor='darkGray',
                width=set_width,
                opacity=0.8
            )
            fig.add_annotation(
                x=set_x_pos,
                y=1-2*spacing,
                xref="paper",
                yref="paper",
                text="Complexity 1-3x > GSV",
                showarrow=False,
                font=dict(
                    size=12,
                    color="#000000"
                ),
                align="left",
                bordercolor="#c7c7c7",
                borderwidth=0,
                borderpad=4,
                bgcolor='darkorange',
                width=set_width,
                opacity=0.8
            )
            fig.add_annotation(
                x=set_x_pos,
                y=1-3*spacing,
                xref="paper",
                yref="paper",
                text="Complexity 3x > GSV",
                showarrow=False,
                font=dict(
                    size=12,
                    color="#ffffff"
                ),
                align="left",
                bordercolor="#c7c7c7",
                borderwidth=0,
                borderpad=4,
                bgcolor='maroon',
                width=set_width,
                opacity=0.8
            )

        col_idx += 1
        height_calc = 30 * len(y_val)
        height_calc = max([height_calc, 600])
        height_calc = min([height_calc, 1500])

    fig = fig.update_xaxes(tickfont=dict(size=12))
    fig = fig.update_yaxes(tickfont=dict(size=12))
    fig = fig.update_layout(showlegend=True)
    fig = fig.update_layout(height=height_calc, width=3 * 400, barmode='stack', showlegend=False,
                            margin=dict(
                                l=50,
                                r=50,
                                b=50,
                                t=50
                            ),
                            yaxis=dict(autorange="reversed"),  # note this will not work for most waterfall charts
                            )

    return fig



# three column waterfall chart to show Pareto charts
def create_waterfall_three_col(control_title="Plot controls: ", data=None,
                               filter_col=None,
                               filter_val=None, filter_lab_col=None,
                               filter_col_2=None, filter_lab_col_2=None, filter_val_2=None,
                               filter_col_3=None, filter_lab_col_3=None, filter_val_3=None,
                               filter_col_4=None, filter_lab_col_4=None, filter_val_4=None,
                               filter_col_5=None, filter_lab_col_5=None, filter_val_5=None,
                               filter_col_6=None, filter_lab_col_6=None, filter_val_6=None,
                               level_list=None, filter_control_title="Select filter value: "):
    graph_id_name = 'dynamic_graphic_' + str(round(random() * 10 ** 6))
    spin_id_name = 'spinner_' + str(round(random() * 10 ** 6))
    
    # REQUIRED COMMENTS
    # print("control_title", control_title)
    # print("filter_col", filter_col)
    # print("filter_col_2", filter_col_2)
    # print("filter_col_3", filter_col_3)
    # print("filter_col_4", filter_col_4)
    # print("filter_col_5", filter_col_5)
    # print("filter_col_6", filter_col_6)
    # print("filter_lab_col", filter_lab_col)
    # print("filter_lab_col_2", filter_lab_col_2)
    # print("filter_lab_col_3", filter_lab_col_3)
    # print("filter_lab_col_4", filter_lab_col_4)
    # print("filter_lab_col_5", filter_lab_col_5)
    # print("filter_lab_col_6", filter_lab_col_6)
    # print("filter_val", filter_val)
    # print("filter_val_2", filter_val_2)
    # print("filter_val_3", filter_val_3)
    # print("filter_val_4", filter_val_4)
    # print("filter_val_5", filter_val_5)
    # print("filter_val_6", filter_val_6)
    # print("level_list", level_list)
    # print("filter_control_title", filter_control_title)
    # OUTPUT
    # control_title Plot controls: 
    # filter_col Portfolio
    # filter_col_2 Category
    # filter_col_3 Brand
    # filter_col_4 SubSBU
    # filter_col_5 SBU
    # filter_col_6 Region
    # filter_lab_col None
    # filter_lab_col_2 None
    # filter_lab_col_3 None
    # filter_lab_col_4 None
    # filter_lab_col_5 None
    # filter_lab_col_6 None
    # filter_val None
    # filter_val_2 None
    # filter_val_3 None
    # filter_val_4 None
    # filter_val_5 None
    # filter_val_6 None
    # level_list ['Category', 'Portfolio', 'Brand', 'BU', 'SBU', 'SubSBU', 'Grouping', 'reg_list', 'Material_base']
    # filter_control_title Select filter value: 

    # PERHAPS ALMOST NEVER USED
    # LIST DIFFERENT FROM ONE COMING FROM WHERE THE FUNCTION IS INVOKED
    # # main code to build the figures and controls goes here -----------------------------------------------------------
    # level_list = ['Category', 'Portfolio', 'Brand', 'BU', 'SBU', 'SubSBU', 'Grouping', 'reg_list', 'Material_base']
    if level_list is None:
        level_list = ['Category', 'Portfolio', 'Brand', 'Grouping', 'reg_list', 'Material_base']

    # TODO : Understand this
    # update the dataframe with any modifications made by users
    # data = update_app_edits(df=data, cataloge_name='master_dataframe_app_update')
    # print ("df_cleaned_post_update_edit SHAPE", data.shape)
    # data.to_csv("df_cleaned_post_update_edit.csv", index=False)
    # data = request

    # API : /pareto_chart_data
    # # response = requests.get('http://localhost:9999/pareto_chart_data', verify=False)
    # start_time = time.time()
    # response = requests.get('https://595c-112-133-244-168.ngrok.io/pareto_chart_data')
    # end_time = time.time()
    # print(f'RESPONSE in {round(end_time-start_time, 3)} seconds')
    # json = response.json()
    # df_temp = pd.DataFrame.from_dict(json)
    # print ("PROCESSED DATA shape", data.shape)
    # print ("API DATA shape", df_temp.shape)
    # data.to_csv("data_dash_app.csv", index=False)
    # df_temp.to_csv("data_api.csv", index=False)
    # areTheseTwoDfSame = data.equals(df_temp)
    # # TODO LATER
    # # TODO these are actually same but diff might be coming becoz of data type or something
    # print ("DATAFRAME TILL THIS POINT ARE EQUAL -> ", areTheseTwoDfSame)

    # build the filters
    # dd_filter_html, filter_input_1, filter_id_1 = dd_build_TEMP(df=data, col=filter_col, col_label=filter_lab_col,
    #                                                        multi_on=True)
    # dd_filter_html_2, filter_input_2, filter_id_2 = dd_build_TEMP(df=data, col=filter_col_2, col_label=filter_lab_col_2,
    #                                                          multi_on=True)
    # dd_filter_html_3, filter_input_3, filter_id_3 = dd_build_TEMP(df=data, col=filter_col_3, col_label=filter_lab_col_3,
    #                                                          multi_on=True)
    # * ORIGINAL
    # dd_filter_html_4, filter_input_4, filter_id_4 = dd_build(df=data, col=filter_col_4, col_label=filter_lab_col_4)
    # dd_filter_html_5, filter_input_5, filter_id_5 = dd_build(df=data, col=filter_col_5, col_label=filter_lab_col_5)
    # * TEMP
    # ! FILTER DATA FROM API
    # # ! API : /pareto_chart_filter_values
    # start_time = time.time()
    # response = requests.get(f'{api_base_url}/pareto_chart_filter_values')
    # end_time = time.time()
    # print(f'RESPONSE in {round(end_time-start_time, 3)} seconds')
    # json = response.json()
    # print ("FILTER JSON", json)
    json = get_pareto_chart_filter_values()
    sbu_data = json["SBU"]
    sub_sbu_data = json["SubSBU"]
    dd_filter_html_4, filter_input_4, filter_id_4 = dd_build_TEMP(col_values=sub_sbu_data)
    dd_filter_html_5, filter_input_5, filter_id_5 = dd_build_TEMP(col_values=sbu_data)

    # dd_filter_html_6, filter_input_6, filter_id_6 = dd_build_TEMP(df=data, col=filter_col_6, col_label=filter_lab_col_6)
    # print ("dd_filter_html", dd_filter_html)
    # print ("filter_input_1", filter_input_1)
    # print ("filter_id_1", filter_id_1)
    # OUTPUT
    # filter_input_1 filter_id_265242.value
    # filter_id_1 filter_id_265242

    # set the options for the levels
    # * ORIGINAL
    # dd_level_html_1, level_input_1, level_id_1 = dd_build(col=level_list, value_index=0, id_pre='level-id')
    # * TEMP
    # dd_level_html_1, level_input_1, level_id_1 = dd_build_TEMP(col=level_list, value_index=0, id_pre='level-id')
    # print ("dd_level_html_1", dd_level_html_1)
    # print ("level_input_1", level_input_1)
    # print ("level_id_1", level_id_1)
    # OUTPUT
    # level_input_1 level-id_146652.value
    # level_id_1 level-id_146652

    # build the titles for the filters in the control panel
    # filter_title_html = title_build(menu_html=dd_filter_html, title_string_list=[filter_control_title, filter_col])
    # filter_title_html_2 = title_build(menu_html=dd_filter_html_2,
    #                                   title_string_list=[filter_control_title, filter_col_2])
    # filter_title_html_3 = title_build(menu_html=dd_filter_html_3,
    #                                   title_string_list=[filter_control_title, filter_col_3])
    filter_title_html_4 = title_build(menu_html=dd_filter_html_4,
                                      title_string_list=[filter_control_title, filter_col_4])
    filter_title_html_5 = title_build(menu_html=dd_filter_html_5,
                                      title_string_list=[filter_control_title, filter_col_5])
    # filter_title_html_6 = title_build(menu_html=dd_filter_html_6,
    #                                   title_string_list=[filter_control_title, filter_col_6])
    # level_title_html_1 = title_build(menu_html=dd_level_html_1, title_string_list=["Select levels for waterfall: "])
    # control_title_html = title_build(menu_html=dd_filter_html, title_string_list=[control_title])

    # print ("filter_title_html", filter_title_html)
    # print ("filter_title_html_2", filter_title_html_2)
    # print ("filter_title_html_3", filter_title_html_3)
    # print ("filter_title_html_4", filter_title_html_4)
    # print ("filter_title_html_5", filter_title_html_5)
    # print ("filter_title_html_6", filter_title_html_6)
    # print ("level_title_html_1", level_title_html_1)
    # filter_title_html Div(children='Select filter value: Portfolio', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # filter_title_html_2 Div(children='Select filter value: Category', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # filter_title_html_3 Div(children='Select filter value: Brand', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # filter_title_html_4 Div(children='Select filter value: SubSBU', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # filter_title_html_5 Div(children='Select filter value: SBU', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # filter_title_html_6 Div(children='Select filter value: Region', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})
    # level_title_html_1 Div(children='Select levels for waterfall: ', style={'color': 'var(--Bold-text)', 'text-align': 'left', 'font weight': '800'})

    # print ("level_title_html_1", level_title_html_1)
    # print ("control_title_html", control_title_html)

    # build the controls panel
    controls = html.Div(
        [
            # control_title_html,
            # level_title_html_1,
            # dd_level_html_1,
            html.P("Selected level for waterfall: Category"),
            # filter_title_html_6,
            # dd_filter_html_6,
            filter_title_html_5,
            dd_filter_html_5,
            filter_title_html_4,
            dd_filter_html_4,
            # filter_title_html_3,
            # dd_filter_html_3,
            # filter_title_html_2,
            # dd_filter_html_2,
            # filter_title_html,
            # dd_filter_html,
        ])
    # controls = html.Div(
    #     [
    #         html.P("FILTERS WILL COME HERE"),
    #     ])

    # print ("controls", controls)

    # dynamically generated chart that is connected to controls that were created above
    dyn_graph = html.Div(
        [
            html.Div(
                [
                    # html.P(title),
                    dcc.Loading(
                        id=spin_id_name,
                        children=[html.Div(dcc.Graph(id=graph_id_name), )],
                        type="default",
                    ),
                ],
                style={
                    "width": "90%",
                    "display": "inline-block",
                    "text-align": "left",
                    "marginBottom": "30px",
                },
            ),
        ],
        className="nine columns chart_div",
        style={"text-align": "center", "height": "100%", "width": "100%"},
    )

    # Call back for building the dynamic chart
    # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_1 = "filter_1_in_pos_1"
    # filter_2_in_pos_1 = "filter_2_in_pos_1"
    # filter_3_in_pos_1 = "filter_3_in_pos_1"
    filter_4_in_pos_1 = "filter_4_in_pos_1"
    filter_5_in_pos_1 = "filter_5_in_pos_1"
    # filter_6_in_pos_1 = "filter_6_in_pos_1"
    # level_input_pos_1 = "level_input_pos_1"

    # input_var_1, var_positions_1 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_1,
    #                                                     input_2=filter_input_2, input_2_name=filter_2_in_pos_1,
    #                                                     input_3=filter_input_3, input_3_name=filter_3_in_pos_1,
    #                                                     input_5=filter_input_4, input_5_name=filter_4_in_pos_1,
    #                                                     input_6=filter_input_5, input_6_name=filter_5_in_pos_1,
    #                                                     input_7=filter_input_6, input_7_name=filter_6_in_pos_1,
    #                                                     input_4=level_input_1, input_4_name=level_input_pos_1,
    #                                                     )
    input_var_1, var_positions_1 = build_callback_input(
                                                        # input_1=filter_input_1, input_1_name=filter_1_in_pos_1,
                                                        # input_2=filter_input_2, input_2_name=filter_2_in_pos_1,
                                                        # input_3=filter_input_3, input_3_name=filter_3_in_pos_1,
                                                        input_5=filter_input_4, input_5_name=filter_4_in_pos_1,
                                                        input_6=filter_input_5, input_6_name=filter_5_in_pos_1,
                                                        # input_7=filter_input_6, input_7_name=filter_6_in_pos_1,
                                                        # input_4=level_input_1, input_4_name=level_input_pos_1,
                                                        )
    output_var = Output(graph_id_name, 'figure')

    # print ("input_var_1", input_var_1)
    # [<Input `filter_id_568948.value`>, <Input `filter_id_808272.value`>, <Input `filter_id_747434.value`>, <Input `level-id_294618.value`>, <Input `filter_id_248308.value`>, <Input `filter_id_744445.value`>, <Input `filter_id_39855.value`>]
    # print ("var_positions_1", var_positions_1)
    # {'filter_1_in_pos_1': 0, 'filter_2_in_pos_1': 1, 'filter_3_in_pos_1': 2, 'level_input_pos_1': 3, 'filter_4_in_pos_1': 4, 'filter_5_in_pos_1': 5, 'filter_6_in_pos_1': 6}

    @app.callback(Output(spin_id_name, "children"))
    @app.callback(output_var, input_var_1)
    def update_graph(*args):
        print("FILTERS CHANGED hence CALLBACK TRIGGERED")
        # print("args", args)

        # put the vars in a list to select using position variable just created
        dyn_vars = args
        # df = data
        # ('AIS', 'PTG')
        # sub_sbu_filter_val = dyn_vars[0] if dyn_vars[0] is not None else "null"
        sub_sbu_filter_val = dyn_vars[0]
        sbu_filter_val = dyn_vars[1]
        # print ("sbu_filter_val", sbu_filter_val)
        # print ("sub_sbu_filter_val", sub_sbu_filter_val)
        user_selected_filters = {"SBU":sbu_filter_val, "SubSBU":sub_sbu_filter_val}
        print ("user_selected_filters", user_selected_filters)

        # # # ! API : /pareto_chart_data
        # response = requests.post(f'{api_base_url}/pareto_chart_data', json = {"filters":user_selected_filters})
        # json = response.json()
        payload = {"filters":user_selected_filters}
        json = get_pareto_chart_data_from_db(payload)
        # print (json)
        # print (len(json))
        # if len(json) == 0:
        #     print ("I CAME HERE")
        #     fig = html.P("No data for selected filters. Please change the filters"),
        #     return fig
        # print ("json", json)
        # start_time = time.time()
        # response = requests.get('https://595c-112-133-244-168.ngrok.io/pareto_chart_data')

        # ! FILTER THE DATA
        # dynamically set the variables based on position variable previously defined
        # df, filter_name = dd_filter(df=df, col=filter_col, input_pos=var_positions_1.get(filter_1_in_pos_1),
        #                             dyn_vars=dyn_vars, default_val=filter_val)
        # print("df", df.shape)
        # print("filter_name", filter_name)

        # df, filter_name = dd_filter(df=df, col=filter_col_2, input_pos=var_positions_1.get(filter_2_in_pos_1),
        #                             dyn_vars=dyn_vars, default_val=filter_val_2)
        # print("df", df.shape)
        # print("filter_name", filter_name)

        # df, filter_name = dd_filter(df=df, col=filter_col_3, input_pos=var_positions_1.get(filter_3_in_pos_1),
        #                             dyn_vars=dyn_vars, default_val=filter_val_3)
        # print("df", df.shape)
        # print("filter_name", filter_name)

        # ! SQL QUERY FOR FILTER
        # sql_filter_query = dd_filter_TEMP_QUERY_GEN(col_val=sbu_filter_val, col_name="SBU", sql_filter_query="")
        # sql_filter_query = dd_filter_TEMP_QUERY_GEN(col_val=sub_sbu_filter_val, col_name="SubSBU", sql_filter_query="")
        # print ("sql_filter_query", sql_filter_query)
        # print("df", df.shape)

        # df, filter_name_4 = dd_filter(df=df, col=filter_col_4, input_pos=var_positions_1.get(filter_4_in_pos_1),
        #                               dyn_vars=dyn_vars, default_val=filter_val_4)
        # print("df", df.shape)
        # print("filter_name_4", filter_name_4)

        # df, filter_name_5 = dd_filter(df=df, col=filter_col_5, input_pos=var_positions_1.get(filter_5_in_pos_1),
        #                               dyn_vars=dyn_vars, default_val=filter_val_5)
        # print("df", df.shape)
        # print("filter_name_5", filter_name_5)

        # df, filter_name_6 = dd_filter(df=df, col=filter_col_6, input_pos=var_positions_1.get(filter_6_in_pos_1),
        #                               dyn_vars=dyn_vars, default_val=filter_val_6)
        # print("df", df.shape)
        # print("filter_name_6", filter_name_6)        

        # ! FILTER THE DATA
        # level_input_select_1 = dyn_vars[var_positions_1.get(level_input_pos_1)] if level_input_pos_1 is not None else \
        #     level_list[0]
        # ! HARD CODING THIS AS CATEGORY
        level_input_select_1 = "Category"
        print ("level_input_select_1", level_input_select_1)

        value_col_1 = 'Gbl Prev 12Mo GSV $'
        value_col_2 = 'Gbl Prev 12Mo Margin ($)'
        value_col_3 = 'Material'

        value_cols = [value_col_1, value_col_2, value_col_3]

        # ! SUBSET COLUMNS
        # ! AGGREGRATE
        # print("before agg", df.shape)


        # temp = df[[level_input_select_1, 'Gbl Prev 12Mo GSV $', 'Gbl Prev 12Mo Qty',
        #            'Gbl Prev 12Mo Margin ($)', 'Material', 'Material_base'
        #            ]].groupby(level_input_select_1).agg({'Gbl Prev 12Mo GSV $': 'sum',
        #                                                  'Gbl Prev 12Mo Qty': 'sum',
        #                                                  'Gbl Prev 12Mo Margin ($)': 'sum',
        #                                                  'Material': 'nunique',
        #                                                  'Material_base': 'nunique'}).reset_index()
        # print("after agg", temp.shape)
        # print("temp columns", temp.columns)
        # print("value_cols", value_cols)
        #  ! SORT WILL HAPPEN IN DB
        # temp = temp.sort_values(value_cols[0], ascending=False)

        temp = pd.DataFrame.from_dict(json)
        # temp.to_csv("final_pareto_chart.csv", index=False)

        # * ALL THE BELOW CAN HAPPEN HERE AS IT'S UI LOGIC
        for val_col in value_cols:
            val_col_cum_sum = val_col + '_cum_sum'
            val_col_percent_sum = val_col + '_percent_sum'
            val_col_percent = val_col + '_percent'
            val_col_format = val_col + '_format'
            temp[val_col_format] = temp[val_col].apply(human_format)
            temp[val_col_cum_sum] = temp[val_col].cumsum()
            temp[val_col_cum_sum + '_format'] = temp[val_col_cum_sum].apply(human_format)
            temp[val_col_percent_sum] = temp[val_col].cumsum() / temp[val_col].sum()
            temp[val_col_percent] = temp[val_col] / temp[val_col].sum()
            temp[val_col + '_color'] = 'blue'
            temp.loc[temp[val_col_percent_sum] >= 0.95, val_col + '_color'] = 'maroon'
            temp.loc[temp[val_col_percent_sum] < 0.95, val_col + '_color'] = 'darkorange'
            temp.loc[temp[val_col_percent_sum] < 0.80, val_col + '_color'] = 'green'
        all_color_col = 'all_color'
        color_ratio_col = 'ratio_color'
        temp[all_color_col] = 'blue'
        temp[color_ratio_col] = (temp[value_col_3 + '_percent']) / (temp[value_col_1 + '_percent'])
        temp.loc[temp[color_ratio_col] >= 3, all_color_col] = 'maroon'
        temp.loc[temp[color_ratio_col] < 3, all_color_col] = 'darkorange'
        temp.loc[temp[color_ratio_col] < 1, all_color_col] = 'darkGray'
        temp.loc[temp[color_ratio_col] < .5, all_color_col] = 'Green'
        print("just before sending the data for making graph", temp.shape)
        figure = waterfall_chart_multi_col(df=temp,
                                           level_input_select_1=level_input_select_1,
                                           value_cols=value_cols,
                                           orientation_mode='h')
        # figure = "<html>HELLO WORLD</html>"
        return figure

    # # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_f1 = "filter_1_in_pos_f1"
    # filter_2_in_pos_f1 = "filter_2_in_pos_f1"
    # filter_3_in_pos_f1 = "filter_3_in_pos_f1"
    # filter_4_in_pos_f1 = "filter_4_in_pos_f1"
    # filter_5_in_pos_f1 = "filter_5_in_pos_f1"
    # filter_6_in_pos_f1 = "filter_6_in_pos_f1"

    # input_var_f1, var_positions_f1 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_f1,
    #                                                       input_2=filter_input_2, input_2_name=filter_2_in_pos_f1,
    #                                                       input_3=filter_input_3, input_3_name=filter_3_in_pos_f1,
    #                                                       input_4=filter_input_4, input_4_name=filter_4_in_pos_f1,
    #                                                       input_5=filter_input_5, input_5_name=filter_5_in_pos_f1,
    #                                                       input_6=filter_input_6, input_6_name=filter_6_in_pos_f1)
    # output_var_f1 = Output(filter_id_1, 'options')

    # @app.callback(output_var_f1, input_var_f1)
    # def update_radio(*args):
    #     print("update_radio CALLED")
    #     print("args", args)
    #     # put the vars in a list to select using position variable just created
    #     dyn_vars = args
    #     return dd_filter_callback(data=data, dyn_vars=dyn_vars,
    #                               var_pos=var_positions_f1,
    #                               filter_col_in=[filter_col_2, filter_col_3, filter_col_4, filter_col_5,
    #                                              filter_col_6],
    #                               filter_in_pos=[filter_2_in_pos_f1, filter_3_in_pos_f1, filter_4_in_pos_f1,
    #                                              filter_5_in_pos_f1, filter_6_in_pos_f1],
    #                               filter_val_in=[filter_val_2, filter_val_3, filter_val_4, filter_val_5,
    #                                              filter_val_6],
    #                               filter_col_out=[filter_col],
    #                               filter_col_lab_out=[filter_lab_col])

    # # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_f2 = "filter_1_in_pos_f2"
    # filter_2_in_pos_f2 = "filter_2_in_pos_f2"
    # filter_3_in_pos_f2 = "filter_3_in_pos_f2"
    # filter_4_in_pos_f2 = "filter_4_in_pos_f2"
    # filter_5_in_pos_f2 = "filter_5_in_pos_f2"
    # filter_6_in_pos_f2 = "filter_6_in_pos_f2"
    # input_var_f2, var_positions_f2 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_f2,
    #                                                       input_2=filter_input_2, input_2_name=filter_2_in_pos_f2,
    #                                                       input_3=filter_input_3, input_3_name=filter_3_in_pos_f2,
    #                                                       input_4=filter_input_4, input_4_name=filter_4_in_pos_f2,
    #                                                       input_5=filter_input_5, input_5_name=filter_5_in_pos_f2,
    #                                                       input_6=filter_input_6, input_6_name=filter_6_in_pos_f2)

    # output_var_f2 = Output(filter_id_2, 'options')

    # @app.callback(output_var_f2, input_var_f2)
    # def update_radio(*args):
    #     print("update_radio 2 CALLED")
    #     print("args", args)
    #     # put the vars in a list to select using position variable just created
    #     dyn_vars = args
    #     return dd_filter_callback(data=data, dyn_vars=dyn_vars,
    #                               var_pos=var_positions_f2,
    #                               filter_col_in=[filter_col_3, filter_col_4, filter_col_5, filter_col_6],
    #                               filter_in_pos=[filter_3_in_pos_f2, filter_4_in_pos_f2, filter_5_in_pos_f2,
    #                                              filter_6_in_pos_f2],
    #                               filter_val_in=[filter_val_3, filter_val_3, filter_val_4, filter_val_5,
    #                                              filter_val_6],
    #                               filter_col_out=[filter_col_2],
    #                               filter_col_lab_out=[filter_lab_col_2])

    # # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_f3 = "filter_1_in_pos_f3"
    # filter_2_in_pos_f3 = "filter_2_in_pos_f3"
    # filter_3_in_pos_f3 = "filter_3_in_pos_f3"
    # filter_4_in_pos_f3 = "filter_4_in_pos_f3"
    # filter_5_in_pos_f3 = "filter_5_in_pos_f3"
    # filter_6_in_pos_f3 = "filter_6_in_pos_f3"
    # input_var_f3, var_positions_f3 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_f3,
    #                                                       input_2=filter_input_2, input_2_name=filter_2_in_pos_f3,
    #                                                       input_3=filter_input_3, input_3_name=filter_3_in_pos_f3,
    #                                                       input_4=filter_input_4, input_4_name=filter_4_in_pos_f3,
    #                                                       input_5=filter_input_5, input_5_name=filter_5_in_pos_f3,
    #                                                       input_6=filter_input_6, input_6_name=filter_6_in_pos_f3)

    # output_var_f3 = Output(filter_id_3, 'options')

    # @app.callback(output_var_f3, input_var_f3)
    # def update_radio(*args):
    #     print("update_radio 3 CALLED")
    #     print("args", args)
    #     # put the vars in a list to select using position variable just created
    #     dyn_vars = args
    #     return dd_filter_callback(data=data, dyn_vars=dyn_vars,
    #                               var_pos=var_positions_f3,
    #                               filter_col_in=[filter_col_4, filter_col_5, filter_col_6],
    #                               filter_in_pos=[filter_4_in_pos_f3, filter_5_in_pos_f3, filter_6_in_pos_f3],
    #                               filter_val_in=[filter_val_4, filter_val_5, filter_val_6],
    #                               filter_col_out=[filter_col_3],
    #                               filter_col_lab_out=[filter_lab_col_3])

    # # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_f4 = "filter_1_in_pos_f4"
    # filter_2_in_pos_f4 = "filter_2_in_pos_f4"
    # filter_3_in_pos_f4 = "filter_3_in_pos_f4"
    # filter_4_in_pos_f4 = "filter_4_in_pos_f4"
    # filter_5_in_pos_f4 = "filter_5_in_pos_f4"
    # filter_6_in_pos_f4 = "filter_6_in_pos_f4"
    # input_var_f4, var_positions_f4 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_f4,
    #                                                       input_2=filter_input_2, input_2_name=filter_2_in_pos_f4,
    #                                                       input_3=filter_input_3, input_3_name=filter_3_in_pos_f4,
    #                                                       input_4=filter_input_4, input_4_name=filter_4_in_pos_f4,
    #                                                       input_5=filter_input_5, input_5_name=filter_5_in_pos_f4,
    #                                                       input_6=filter_input_6, input_6_name=filter_6_in_pos_f4)

    # output_var_f4 = Output(filter_id_4, 'options')

    # @app.callback(output_var_f4, input_var_f4)
    # def update_radio(*args):
    #     print("update_radio 4 CALLED")
    #     print("args", args)
    #     # put the vars in a list to select using position variable just created
    #     dyn_vars = args
    #     return dd_filter_callback(data=data, dyn_vars=dyn_vars,
    #                               var_pos=var_positions_f4,
    #                               filter_col_in=[filter_col_5, filter_col_6],
    #                               filter_in_pos=[filter_5_in_pos_f4, filter_6_in_pos_f4],
    #                               filter_val_in=[filter_val_5, filter_val_6],
    #                               filter_col_out=[filter_col_4],
    #                               filter_col_lab_out=[filter_lab_col_4])

    # # build the inputs for the callback; note that these need to be different than the other call backs and the current
    # # build_callback_input function is set up to take up to 14 arguments
    # filter_1_in_pos_f5 = "filter_1_in_pos_f5"
    # filter_2_in_pos_f5 = "filter_2_in_pos_f5"
    # filter_3_in_pos_f5 = "filter_3_in_pos_f5"
    # filter_4_in_pos_f5 = "filter_4_in_pos_f5"
    # filter_5_in_pos_f5 = "filter_5_in_pos_f5"
    # filter_6_in_pos_f5 = "filter_6_in_pos_f5"
    # input_var_f5, var_positions_f5 = build_callback_input(input_1=filter_input_1, input_1_name=filter_1_in_pos_f5,
    #                                                       input_2=filter_input_2, input_2_name=filter_2_in_pos_f5,
    #                                                       input_3=filter_input_3, input_3_name=filter_3_in_pos_f5,
    #                                                       input_4=filter_input_4, input_4_name=filter_4_in_pos_f5,
    #                                                       input_5=filter_input_5, input_5_name=filter_5_in_pos_f5,
    #                                                       input_6=filter_input_6, input_6_name=filter_6_in_pos_f5)

    # output_var_f5 = Output(filter_id_5, 'options')

    # @app.callback(output_var_f5, input_var_f5)
    # def update_radio(*args):
    #     print("update_radio 5 CALLED")
    #     print("args", args)
    #     # put the vars in a list to select using position variable just created
    #     dyn_vars = args
    #     return dd_filter_callback(data=data, dyn_vars=dyn_vars,
    #                               var_pos=var_positions_f5,
    #                               filter_col_in=[filter_col_6],
    #                               filter_in_pos=[filter_6_in_pos_f5],
    #                               filter_val_in=[filter_val_6],
    #                               filter_col_out=[filter_col_5],
    #                               filter_col_lab_out=[filter_lab_col_5])

    print ("JUST BEFORE return inside create_waterfall_three_col")
    return controls, dyn_graph

# helper functions to simplify code -----------------------------------------------------------------------------------

# function to filter based on dropdown
def dd_filter(df, col, input_pos, dyn_vars, default_val):
    # print ("dd_filter arguments") 
    # print ("df.shape", df.shape) # df.shape (24306, 68)
    # print ("col", col) # col Region
    # print ("input_pos", input_pos) # input_pos 5
    # print ("dyn_vars", dyn_vars) # dyn_vars (None, None, None, None, None, None)
    # print ("default_val", default_val) # default_val None
    """
    Filter a data set based on input from a dropdown filter based on a call back if filter value is not None

    This function uses a dataframe and a column to filter the dataframe it determines if there is any value to filter
    on and returns the filtered data otherwise it returns the data unfiltered
    """
    # ! SQL FILTER QUERY
    sql_query = ""
    df_col_mapping = {"Region":"reg_list"}
    if col is not None:
        # TODO: A little complicated query
        if (col.upper() == 'REGION') | (col.upper() == 'REGIONS') | (col.upper() == 'REG_LIST'):
            val = dyn_vars[input_pos] if input_pos is not None else None
            if val is not None:
                df['regions'] = df['reg_list'].str.split("_")
                df = df[~(df['regions'].isnull())]
                df = df[df['regions'].apply(lambda x: val in x)] if val is not None else df
            filter_name = val
        # * DONE
        else:
            val = dyn_vars[input_pos] if input_pos is not None else None if default_val is None else default_val
            if val is not None:
                # Only if val is not null, frame the query
                if isinstance(val, list):
                    index_bool_false = df[col] == ''
                    index_bool = index_bool_false
                    filter_name = None
                    for each_val in val:
                        if each_val in df[col].unique():
                            index_bool_temp = df[col] == each_val if each_val is not None else index_bool_false
                            index_bool = index_bool | index_bool_temp
                            filter_name = each_val
                        else:
                            filter_name = None if filter_name is None else filter_name
                    df = df[index_bool] if any(index_bool) else df
                else:
                    sql_query = f"{sql_query} AND WHERE {col} = {val}"
                    if val in df[col].unique():
                        df = df[df[col] == val] if val is not None else df
                        filter_name = val
                    else:
                        filter_name = None
            else:
                filter_name = None
    else:
        filter_name = None
    return df, filter_name

# function to filter based on dropdown
def dd_filter_TEMP_QUERY_GEN(col_val="PTG", col_name="SBU", sql_filter_query=""):
    # print ("dd_filter arguments") 
    # print ("df.shape", df.shape) # df.shape (24306, 68)
    # print ("col", col) # col Region
    # print ("input_pos", input_pos) # input_pos 5
    # print ("dyn_vars", dyn_vars) # dyn_vars (None, None, None, None, None, None)
    # print ("default_val", default_val) # default_val None
    """
    Filter a data set based on input from a dropdown filter based on a call back if filter value is not None

    This function uses a dataframe and a column to filter the dataframe it determines if there is any value to filter
    on and returns the filtered data otherwise it returns the data unfiltered
    """
    # ! SQL FILTER QUERY
    sql_query = ""
    if col_val is not None:
        # print ("col_val", col_val)
        sql_query = f"{sql_query} WHERE {col_name} = {col_val} AND"
    return sql_query


# build options for dropdown lists
def dd_build_options(df=None, col=None, col_label=None):
    """
    Function that builds the dropdown options for a filter given a dataframe and filter column

    :param df: dataframe that will be used to create filter options
    :param col: column within the data frame to build the filter; function will take the unique values
    :param col_label: labels for the filter options; if this is none the values will be used as labels
    :return: a list of options that can be added to a dash dropDown object
    """
    if df is None:
        if col_label is not None:
            temp_df = pd.DataFrame([col, col_label])
            dd_options = [{'label': i[2], 'value': i[1]} for i in temp_df.itertuples()]
        else:
            dd_options = [{'label': i, 'value': i} for i in col]
    else:
        if col_label is not None:
            temp_df = df[[col, col_label]]
            temp_df = temp_df.dropna()
            dd_options = [{'label': i[2], 'value': i[1]} for i in temp_df.itertuples()]
        else:
            temp_df = df[[col]]
            temp_df = temp_df.dropna()
            dd_options = [{'label': i, 'value': i} for i in temp_df[col].unique()]

    return dd_options


# helper function to build dropdown menus
def dd_build(df=None, col=None, col_label=None, value_default=None, value_index=None, id_pre='filter_id',
             multi_on=False, is_state=False):
    distinct_filter_id = str(round(random() * 10 ** 6))
    filter_id = id_pre + '_' + distinct_filter_id
    if col is not None:
        if (col == 'Region') | (col == 'region') | (col == 'Regions') | (col == 'regions') | (col == 'reg_list'):
            df['regions'] = df['reg_list'].str.split("_")
            df = df[~(df['regions'].isnull())]
            drop_down_option_list = set(list(np.concatenate(df['regions'].values)))
            if 'NA' in drop_down_option_list:
                drop_down_option_list.remove('NA')
            dd_options = dd_build_options(df=None, col=drop_down_option_list, col_label=col_label)
        else:
            # build the options using a label if needed
            dd_options = dd_build_options(df=df, col=col, col_label=col_label)
        if value_index is not None:
            if (value_index == 'All') | (value_index == 'all'):
                value_default = [x['value'] for x in dd_options]
            else:
                value_default = dd_options[value_index]['value']
        # print("col", col)
        # print("filter_id", filter_id)
        # print("col_label", col_label)
        # print("dd_options", dd_options)
        # print("value_default", value_default)
        # print("multi_on", multi_on)
        dd_filter_html = dcc.Dropdown(
            id=filter_id,
            options=dd_options,
            value=value_default,
            multi=multi_on
        )
        if is_state:
            filter_input = [Input(filter_id, 'value'), State(filter_id, 'value')]
        else:
            filter_input = Input(filter_id, 'value')

        # embed dropdown in div
        dd_filter_html = html.Div([
            dd_filter_html
        ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
    else:
        dd_filter_html = None
        filter_input = None
    return dd_filter_html, filter_input, filter_id

def dd_build_options_TEMP(col_val):
    options = []
    for value in col_val:
        options.append({"label":value, "value":value})
    return options

# helper function to build dropdown menus
def dd_build_TEMP(col_values=['PTG', "FSL"],id_pre='filter_id',multi_on=False, is_state=False, value_default="PTG"):
    col_name = "SBU"
    value_default = None
    dd_options = dd_build_options_TEMP(col_values)
    # print ("dd_options", dd_options)
    distinct_filter_id = str(round(random() * 10 ** 6))
    filter_id = id_pre + '_' + distinct_filter_id
    dd_filter_html = dcc.Dropdown(
                            id=filter_id,
                            options=dd_options,
                            value=value_default,
                            multi=multi_on
                        )
    if is_state:
        filter_input = [Input(filter_id, 'value'), State(filter_id, 'value')]
    else:
        filter_input = Input(filter_id, 'value')
    # print ("dd_options", dd_options)
    return dd_filter_html, filter_input, filter_id


# build a radio option toggle
def toggle_build(option_lists=None, value_default=None, id_pre='toggle-id', is_state=False):
    distinct_id = str(round(random() * 10 ** 6))
    toggle_id = id_pre + distinct_id
    toggle_html = dcc.RadioItems(
        id=toggle_id,
        options=[{'label': i, 'value': i} for i in option_lists],
        value=value_default,
        labelStyle={'display': 'inline-block'}
    )
    # embed toggle in div
    toggle_html = html.Div([
        toggle_html
    ], style={'width': '95%', "display": "inline-block", "text-align": "left"})

    if is_state:
        toggle_input = [Input(toggle_id, 'value'), State(toggle_id, 'value')]
    else:
        toggle_input = Input(toggle_id, 'value')

    return toggle_html, toggle_input, toggle_id


# create an html title
def title_build(menu_html=None, title_string_list=None):
    if menu_html is not None:
        title_html = html.Div(''.join(title_string_list), style={"color": "var(--Bold-text)", "text-align": "left",
                                                                 "font weight": "800"})
    else:
        title_html = None

    return title_html


# helper function to format large number strings e.g. 1,000 -> 1K, 1,000,000 -> 1M etc
def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.1f%s' % (num, ['', 'K', 'M', 'B', 'T', 'Q'][magnitude])


# table html
def build_sku_list_table(spin_id_name, graph_id_name, out_cols, editable_val=False):
    # build the column options
    if 'Images' in out_cols:
        image_opt_dict = [{"name": i,
                           "id": i,
                           'type': 'text',
                           'presentation': 'markdown',
                           "editable": False}
                          for i in ['Images']]
    else:
        image_opt_dict = []

    if 'Add Notes' in out_cols:
        notes_opt_dict = [{"name": i,
                           "id": i,
                           'presentation': 'dropdown',
                           "clearable": False}
                          for i in ['Add Notes']]
    else:
        notes_opt_dict = []

    editable_cols = ['Grouping', 'Segment 1', 'Segment 2', 'Segment 3', 'Segment 4', 'Segment 5',
                     'Segment 6', 'Segment 7', 'Segment 8', 'Segment 9', 'Segment 10']
    editable_opt_dict = [{"name": i,
                          "id": i,
                          "editable": True}
                         for i in editable_cols]
    remove_list = editable_cols + ['Images'] + ['Add Notes']
    other_cols = [i for i in out_cols if i not in remove_list]
    other_opt_dict = [{"name": i,
                       "id": i,
                       "editable": False}
                      for i in other_cols]

    column_options = other_opt_dict + notes_opt_dict + editable_opt_dict + image_opt_dict

    # build the table
    table_html = dcc.Loading(id=spin_id_name, children=[html.Div(
        dash_table.DataTable(id=graph_id_name,
                             columns=column_options,
                             editable=editable_val,
                             dropdown={
                                 'Add Notes': {
                                     'options': [
                                         {'label': i, 'value': i}
                                         for i in pd.Series(['Review', 'Keep', 'Remove'])
                                     ],
                                     "clearable": False
                                 },
                             },
                             style_as_list_view=True,
                             style_cell={
                                 'padding': '5px',
                                 'whiteSpace': 'normal',
                                 'height': 'auto',
                                 'textAlign': 'left',
                                 'fontSize': 10,
                                 'font-family': 'Helvetica Roman sans-serif'
                             },
                             style_header={
                                 'backgroundColor': '#333',
                                 'fontWeight': 'bold',
                                 'color': '#ffdb0a',
                                 'fontSize': 12,
                             },
                             style_table={'overflowX': 'auto',
                                          'minHeight': '100%',
                                          'height': '100%',
                                          'overflowY': 'auto'},
                             style_data_conditional=[
                                 {
                                     'if': {'row_index': 'odd'},
                                     'backgroundColor': '#f7ecb5'
                                 }
                             ],
                             filter_action='native',
                             sort_action='native',
                             sort_mode='multi',
                             fixed_rows={'headers': True},
                             export_format='xlsx',
                             export_headers='display',
                             merge_duplicate_headers=True
                             ),
    )], type="default")

    return table_html


# table format dataframe
def build_sku_list_dataframe(df, out_cols):
    out_put = df
    if 'Material' in list(df.columns):
        if 'Component material' in list(df.columns):
            out_put = out_put.sort_values(by=['Material', "Component material"])
        else:
            out_put = out_put.sort_values(by=['Material'])

    if 'ave_sales_price' in list(df.columns):
        out_put = out_put.round({'ave_sales_price': 2})
    if 'images' in list(df.columns):
        out_put['Image'] = display_links(out_put['images'])
    data_dict = out_put[out_cols]
    data_dict = data_dict.drop_duplicates()

    return data_dict.to_dict('records')


# format dataframe column of urls so that it displays as hyperlink
def display_links(links):
    links = links.astype('str').str.replace('\'\', ', '')
    links = links.str.replace('\'', '')
    links = links.str.replace(',', '')
    links = links.str.replace('[', '')
    links = links.str.replace(']', '')
    test = re.compile('[0-9]*x[0-9]*')
    links = links.to_list()
    rows = []
    for x in links:
        link = ''
        if len(x.split(" ")) > 1:
            for y in x.split(" "):
                size = test.findall(y)
                size = [a.split("x")[0] for a in size]
                if len(size) > 0:
                    link = link + ' [Link ' + size[0] + 'px](' + str(y) + ')'
                else:
                    link = link + ' [Link](' + str(y) + ')'
        rows.append(link)
    return rows


# get the levels from dropdown
def get_tree_levels(dyn_vars, input_pos_1=None, input_pos_2=None, input_pos_3=None, input_pos_4=None, input_pos_5=None,
                    input_pos_6=None, input_pos_7=None, input_pos_8=None, input_pos_9=None, input_pos_10=None,
                    flip_list=False):
    level_input_select_1 = dyn_vars[input_pos_1] if input_pos_1 is not None else False
    level_input_select_2 = dyn_vars[input_pos_2] if input_pos_2 is not None else False
    level_input_select_3 = dyn_vars[input_pos_3] if input_pos_3 is not None else False
    level_input_select_4 = dyn_vars[input_pos_4] if input_pos_4 is not None else False
    level_input_select_5 = dyn_vars[input_pos_5] if input_pos_5 is not None else False
    level_input_select_6 = dyn_vars[input_pos_6] if input_pos_6 is not None else False
    level_input_select_7 = dyn_vars[input_pos_7] if input_pos_7 is not None else False
    level_input_select_8 = dyn_vars[input_pos_8] if input_pos_8 is not None else False
    level_input_select_9 = dyn_vars[input_pos_9] if input_pos_9 is not None else False
    level_input_select_10 = dyn_vars[input_pos_10] if input_pos_10 is not None else False

    levels_selected = []
    if level_input_select_1:
        levels_selected.append(level_input_select_1)
    if level_input_select_2:
        levels_selected.append(level_input_select_2)
    if level_input_select_3:
        levels_selected.append(level_input_select_3)
    if level_input_select_4:
        levels_selected.append(level_input_select_4)
    if level_input_select_5:
        levels_selected.append(level_input_select_5)
    if level_input_select_6:
        levels_selected.append(level_input_select_6)
    if level_input_select_7:
        levels_selected.append(level_input_select_7)
    if level_input_select_8:
        levels_selected.append(level_input_select_8)
    if level_input_select_9:
        levels_selected.append(level_input_select_9)
    if level_input_select_10:
        levels_selected.append(level_input_select_10)

    levels = pd.Series(levels_selected).unique().tolist()
    if flip_list:
        levels = list(reversed(levels))

    return levels


# this function is built to create input variables for dynamic call backs; this can probably be improved using **kwargs
def build_callback_input(input_1=None, input_1_name=None, input_2=None, input_2_name=None, input_3=None,
                         input_3_name=None, input_4=None, input_4_name=None, input_5=None, input_5_name=None,
                         input_6=None, input_6_name=None, input_7=None, input_7_name=None, input_8=None,
                         input_8_name=None, input_9=None, input_9_name=None, input_10=None, input_10_name=None,
                         input_11=None, input_11_name=None, input_12=None, input_12_name=None,
                         input_13=None, input_13_name=None, input_14=None, input_14_name=None,
                         input_15=None, input_15_name=None, input_16=None, input_16_name=None):
    input_var = []
    var_positions = {}
    var_position = 0

    if input_1 is not None:
        input_var.append(input_1)
        var_positions.update({input_1_name: var_position})
        var_position += 1
    if input_2 is not None:
        input_var.append(input_2)
        var_positions.update({input_2_name: var_position})
        var_position += 1
    if input_3 is not None:
        input_var.append(input_3)
        var_positions.update({input_3_name: var_position})
        var_position += 1
    if input_4 is not None:
        input_var.append(input_4)
        var_positions.update({input_4_name: var_position})
        var_position += 1
    if input_5 is not None:
        input_var.append(input_5)
        var_positions.update({input_5_name: var_position})
        var_position += 1
    if input_6 is not None:
        input_var.append(input_6)
        var_positions.update({input_6_name: var_position})
        var_position += 1
    if input_7 is not None:
        input_var.append(input_7)
        var_positions.update({input_7_name: var_position})
        var_position += 1
    if input_8 is not None:
        input_var.append(input_8)
        var_positions.update({input_8_name: var_position})
        var_position += 1
    if input_9 is not None:
        input_var.append(input_9)
        var_positions.update({input_9_name: var_position})
        var_position += 1
    if input_10 is not None:
        input_var.append(input_10)
        var_positions.update({input_10_name: var_position})
        var_position += 1
    if input_11 is not None:
        input_var.append(input_11)
        var_positions.update({input_11_name: var_position})
        var_position += 1
    if input_12 is not None:
        input_var.append(input_12)
        var_positions.update({input_12_name: var_position})
        var_position += 1
    if input_13 is not None:
        input_var.append(input_13)
        var_positions.update({input_13_name: var_position})
        var_position += 1
    if input_14 is not None:
        input_var.append(input_14)
        var_positions.update({input_14_name: var_position})
        var_position += 1
    if input_15 is not None:
        input_var.append(input_15)
        var_positions.update({input_15_name: var_position})
        var_position += 1
    if input_16 is not None:
        input_var.append(input_16)
        var_positions.update({input_16_name: var_position})
        var_position += 1

    return input_var, var_positions


# dynamic filter based on tree click
def tree_click_filter(df=None, dyn_vars=None, var_positions=None, level_1_in_pos=None, level_2_in_pos=None,
                      level_3_in_pos=None, level_4_in_pos=None, level_5_in_pos=None, level_6_in_pos=None,
                      level_7_in_pos=None, table_html_in_pos=None, is_bar=False):
    graph_click = dyn_vars[var_positions.get(table_html_in_pos)]
    if graph_click is not None:
        if is_bar:
            graph_click_current = graph_click.get("points")[0].get("x")
            print(graph_click)
            print(graph_click_current)
            val = graph_click_current
            col = level_1_in_pos
            if val in df[col].unique():
                df = df[df[col] == val] if val is not None else df
        else:
            levels = get_tree_levels(dyn_vars=dyn_vars, input_pos_1=var_positions.get(level_1_in_pos),
                                     input_pos_2=var_positions.get(level_2_in_pos),
                                     input_pos_3=var_positions.get(level_3_in_pos),
                                     input_pos_4=var_positions.get(level_4_in_pos),
                                     input_pos_5=var_positions.get(level_5_in_pos),
                                     input_pos_6=var_positions.get(level_6_in_pos),
                                     input_pos_7=var_positions.get(level_7_in_pos))
            graph_click_path = graph_click.get("points")[0].get("currentPath").split("/")
            graph_click_current = graph_click.get("points")[0].get("label")
            if len(graph_click_path) > 2:
                filter_val_list = graph_click_path[1:-1]
            else:
                filter_val_list = []
            filter_val_list.append(graph_click_current)
            filter_col_list = levels[:len(filter_val_list)]
            for i, val in enumerate(filter_val_list):
                col = filter_col_list[i]
                if val in df[col].unique():
                    df = df[df[col] == val] if val is not None else df

    return df


# function to calculate the similarity in two bom
def calc_common_bom(df, material_1, material_2):
    if material_1 == material_2:
        percent_common_1 = 1
        percent_common_2 = 1
    else:
        temp_1 = set(df[df['Material'] == material_1]['Component material'])
        temp_2 = set(df[df['Material'] == material_2]['Component material'])
        if (len(temp_1) > 0) & (len(temp_2) > 0):
            common_elements = list(temp_1 & temp_2)
            percent_common_1 = len(common_elements) / len(temp_1)
            percent_common_2 = len(common_elements) / len(temp_2)
        else:
            percent_common_1 = None
            percent_common_2 = None

    return percent_common_1, percent_common_2


# build callbacks for filtering dropdowns
def dd_filter_callback(data, dyn_vars, var_pos, filter_col_in, filter_in_pos,
                       filter_val_in, filter_col_out, filter_col_lab_out):
    # reassign data frame to local scope
    df = data

    # dynamically set the variables based on position variable previously defined
    idx = 0
    filter_names = []
    for filter_col_id in filter_col_in:
        df, filter_name = dd_filter(df=df, col=filter_col_id, input_pos=var_pos.get(filter_in_pos[idx]),
                                    dyn_vars=dyn_vars, default_val=filter_val_in[idx])
        idx += 1
        filter_names.append(filter_name)

    # build the options using a label if needed
    dd_options = dd_build_options(df=df, col=filter_col_out[0], col_label=filter_col_lab_out[0])

    return dd_options


# small helper function to help build lists when the value might be none
def append_not_none(cols_out, col_in):
    """ Appends column name to list if the column name is not none if it is a list then it extends the list"""
    if col_in is not None:
        if isinstance(col_in, str):
            cols_out.append(col_in)
        else:
            cols_out.extend(col_in)
    return cols_out


# def update_app_edits(df, cataloge_name='master_dataframe_app_update'):
#     """ This function replaces values by reading from a table on the server and replacing the values in the dataframe"""
#     server_data = context.catalog.load(cataloge_name)
#     server_data.to_csv("server_data.csv")
#     # print ("server_data.shape",server_data.shape)
#     # print ("dfShape before edit",df.shape)
#     # print ("df col list before edit", df.columns)

#     for col in server_data['update_col'].unique():
#         server_data_mini = server_data[server_data['update_col'] == col]
#         for val in server_data_mini['update_val'].unique():
#             mat_list = server_data_mini[server_data_mini['update_val'] == val]['Material']
#             df.loc[df['Material'].isin(mat_list), col] = val

#     # print ("dfShape after edit", df.shape)
#     # print ("df col list after edit", df.columns)
#     return df


# def update_database_from_table(data_timestamp, table_data, data_previous):
#     # make sure there was actually an update by checking the time stamp; this is a bit redundant with time stamp as
#     # only input variable
#     if data_timestamp is not None:
#         # set up the dataframe to write the update to write the update to
#         columns_out = ['Material', 'update_col', 'update_val', 'update_time', 'is_latest']
#         updated_data = pd.DataFrame(columns=columns_out)
#         updated_data_all = pd.DataFrame(columns=columns_out)

#         # convert the data coming in into dataframes to work with them more easily
#         data_in = pd.DataFrame.from_records(table_data)
#         data_old = pd.DataFrame.from_records(data_previous)

#         # merge the old and new data to find differences
#         data_old.columns = data_old.columns + '_old'
#         data_in_new = data_in.merge(data_old, left_on='Material', right_on='Material_old', how='left').fillna('NaN')

#         # loop over the columns to check if there is anything that has been edited; use write flag to prevent write
#         # if there is no update
#         write = False
#         for col_in in data_in.columns:
#             if ~data_in[col_in].equals(data_old[col_in + '_old']):
#                 # find differences in merged data
#                 data_in_new['is_new'] = ~(data_in_new[col_in] == data_in_new[col_in + '_old'])

#                 # if there are any differences then there is something to write
#                 if data_in_new['is_new'].any():
#                     write = True

#                     # convert the timestamp that will be used to select the latest value that is edited
#                     update_timestamp = pd.to_datetime(data_timestamp, unit='ms')

#                     # loop over all of the changes to write
#                     for value in data_in_new[data_in_new['is_new']][col_in]:
#                         # here we write the ID, the column that was changed, the new value and the time stamp
#                         # note in future versions we should add an ID-type so that you can apply to all in the
#                         # category e.g. set value for brand. This would require the table to be set to a different
#                         # unique value
#                         updated_data['Material'] = data_in_new[data_in_new['is_new']]['Material']
#                         updated_data['update_col'] = col_in
#                         updated_data['update_val'] = value
#                         updated_data['update_time'] = update_timestamp
#                         updated_data['is_latest'] = True
#                         # append this value to the master update so that we can write it once
#                         updated_data_all = updated_data_all.append(updated_data)
#         if write:
#             reset = False
#             if reset:
#                 # reset = False this is here for future use as may need to reset the table
#                 context.catalog.save("master_dataframe_app_update", updated_data_all)
#             else:
#                 # read the data from the catalogue
#                 server_df = context.catalog.load('master_dataframe_app_update')
#                 # append the new data
#                 server_df = server_df.append(updated_data_all)
#                 # get the latest value of the updated data
#                 server_df['is_latest'] = server_df.groupby(['Material', 'update_col'])[
#                                              'update_time'].transform('max') == server_df['update_time']
#                 # write back to the database
#                 context.catalog.save("master_dataframe_app_update", server_df[server_df['is_latest']])
#     return data_timestamp
