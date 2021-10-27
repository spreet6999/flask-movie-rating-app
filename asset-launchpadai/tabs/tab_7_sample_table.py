# -*- coding: utf-8 -*-
# import json
# import math
import numpy as np
import pandas as pd
# import flask
# import dash
from dash.dependencies import Input, Output  # can also import "State" if used in app
import dash_core_components as dcc
import dash_html_components as html
# import plotly.plotly as py
from plotly import graph_objs as go
from apps import template_obj, chart_template, page_template
from app import df_cleaned, context

test = dcc.Markdown('''
This is a list
* **Item 1 has bold text** followed by plain text
* Some Markdown text with _italics_
  * Item 2a
  * Item 2b
''')

data = {'Cap': ['A', 'B', 'C', ], 'non-Cap': ['a', 'b', 'c', ]}
df = pd.DataFrame(data)


# function to build the table for visual efficient assortment
def generate_table(dataframe, max_rows=26):
    brand_col = 'Brand'

    segment_col = 'Segment 4'
    dataframe = dataframe[~(dataframe[brand_col] == 'FACOM')]
    brand_columns = dataframe[brand_col].unique().tolist()
    segment = [''] + dataframe[segment_col].unique().tolist()
    # display_columns = ['images', 'Material', 'Material Desc(CM)',
    #                    'A/B/C/D_Gbl2 (BySBU)', 'ave_sales_price', 'Gbl Prev 12Mo GSV $',
    #                    'Gbl Prev 12Mo Margin ($)', 'Segment 1', 'Segment 2', 'Segment 3',
    #                    'Segment 5', 'Segment 6']
    display_columns = ['images', 'Material', 'Material Desc(CM)', 'Status', 'Replacement',
                       'A/B/C/D_Gbl2 (BySBU)', 'Gbl Prev 12Mo GSV $',
                       'Gbl Prev 12Mo Margin ($)', 'Segment 1', 'Segment 2', 'Segment 3',
                       'Segment 5', 'Segment 6']
    df_selected = dataframe[display_columns + [brand_col, segment_col]]
    count_val = df_selected.groupby([segment_col, brand_col])['Material'].count().reset_index()
    count_val = count_val.groupby([segment_col])['Material'].max().reset_index()

    # series of functions to build the table for EA
    def build_html_body():
        temp = list()
        # loop over the brand rows to build the master table
        for idx in range(min(len(brand_columns), max_rows)):
            temp.append(html.Tr(html_build_cols(i=idx)))
        return temp

    # build the first set of columns - this loops over segments, which should be defined in a function
    def html_build_cols(i):
        temp = list()
        brand = brand_columns[i]

        for col in segment:
            select = (df_selected[brand_col] == brand) & (df_selected[segment_col] == col)
            num_materials = len(df_selected[select]['Material'])
            if col == '':
                content = brand
            else:
                content = html_inner_table(col=col, num_materials=num_materials, select=select)

            temp.append(html.Td(content if (num_materials > 0) | (col == '') | (col == 'categories') else html.Table()))

        return temp

    # build the columns for the internal table
    def html_inner_table(col, num_materials, select, is_category=False):
        temp = list()

        for j in range(len(display_columns)):
            if is_category:
                content = display_columns[j]
            else:
                content = html_ea_content(j=j, col=col, num_materials=num_materials, select=select,
                                          is_category=is_category)
            temp.append(
                html.Table(html.Tr(content), className="table2"))
        return temp

    # build the inner most content
    def html_ea_content(j, col, num_materials, select, is_category):
        temp = list()
        display_col = display_columns[j]
        # if is_category:
        temp.append(html.Td(display_col))
        for k in range(count_val[count_val[segment_col] == col]['Material'].iloc[0]):
            if k < num_materials:
                value_idx = df_selected[select][display_col].to_list()[k]
                image_html = html.Img(src=value_idx, style={'width': '100%'})
                content = html.Td(image_html if j == 0 else value_idx)
            else:
                content = html.Td('')
            temp.append(content)
        return temp

    # build the header
    html_header = [html.Tr([html.Th(col) for col in segment])]

    # build the body
    html_body = build_html_body()

    # combine together to create the output
    html_output = html.Table(
        # Header
        html_header +
        # Body
        html_body, className="table1",
    )

    return html_output


snap_off_knieves_ea = context.catalog.load('snap_off_knieves_ea')
new_header = snap_off_knieves_ea.iloc[0]  # grab the first row for the header
snap_off_knieves_ea = snap_off_knieves_ea[1:]  # take the data less the header row
snap_off_knieves_ea.columns = new_header  # set the header row as the df header

# df_cleaned = df_cleaned[df_cleaned['Portfolio'] == 'SCREWDRIVERS']
# df_cleaned = df_cleaned[df_cleaned['Segment 3'] == 'MULTI BIT']
df_cleaned = df_cleaned[~df_cleaned['Material'].isnull()]
df_cleaned['images'] = df_cleaned['images'].apply(lambda x: list(set(x))[0] if len(set(x)) > 0 else '')

temp = df_cleaned[['Material', 'images', 'A/B/C/D_Gbl2 (BySBU)']]
num_columns = ['Gbl Prev 12Mo GSV $', 'Gbl Prev 12Mo Margin ($)']

df_snap = snap_off_knieves_ea.merge(temp, left_on=['SKU'], right_on=['Material'], how='inner')


def f1(s):
    return max(s.astype(str), key=len)


df_count = df_snap.groupby(['Parent SKU'])['SKU'].count().reset_index()
df_count = df_count.rename(columns={'SKU': 'SKU count'})
df_sum = df_snap[['Parent SKU'] + num_columns].groupby(['Parent SKU']).sum(numeric_only=True).reset_index()
df_desc = df_snap.groupby(['Parent SKU']).agg({'Material Desc(CM)': f1,
                                               'images': f1,
                                               'A/B/C/D_Gbl2 (BySBU)': f1,
                                               'Brand': f1,
                                               'Segment 1': f1,
                                               'Segment 2': f1,
                                               'Segment 3': f1,
                                               'Segment 4': f1,
                                               'Segment 5': f1,
                                               'Segment 6': f1,
                                               'Status': f1,
                                               'Replacement': f1,
                                               })
df_master = df_count.merge(df_sum, left_on=['Parent SKU'], right_on=['Parent SKU'], how='inner')
df_master = df_master.merge(df_desc, left_on=['Parent SKU'], right_on=['Parent SKU'], how='inner')
df_master = df_master.rename(columns={'Parent SKU': 'Material'})

table_layout = html.Div(children=[
    html.H3(children='Visual efficient assortment'),
    generate_table(dataframe=df_master)
], style={"overflow": "scroll", "height": "80vh"})

layout = page_template.layout_left_very_small(page_lead="Test page lead",
                                              left_panel_content=template_obj.title_textbox(title="New Title",
                                                                                            content=test),
                                              right_panel_content=table_layout,
                                              )
