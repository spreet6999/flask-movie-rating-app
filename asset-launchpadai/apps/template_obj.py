# import the libraries used
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from random import random
import plotly.graph_objs as go

# df = pd.read_csv('data/gdp-life-exp-2007.csv')


# a simple function to take the text and put it into a paragraph (html.P) div
def paragraph_textbox(paragraph="Put the content here"):
    return html.Div(
                [
                    html.P(
                        paragraph
                    ),
                ], style={'width': '95%', "display": "inline-block", "text-align": "left"})


# this function creates a text box with a colored block where the title is placed
def title_textbox(title="Put box title here",
                  content=html.P("Put the content here")
                  ):

    layout = html.Div(
                [
                    html.Div(
                        [
                            # title row
                            html.Div(
                                [
                                    html.Div(title, style={"color": "var(--Primary-text)", "text-align": "left", "font weight": "800"}),
                                ],
                                className="row",
                                style={
                                    "padding": 8,
                                    "marginBottom": 5,
                                    "backgroundColor": "var(--Primary-background)",
                                    "borderRadius": "0px"
                                },
                            ),
                            html.Div(
                                [
                                    content

                                ], style={'width': '95%', "display": "inline-block", "text-align": "left"}),
                        ]),
                ])

    return layout


# this function a simple textbox with just a blank div
def blank_textbox(content=html.P("Put the content here")
                  ):

    layout = html.Div(
                [
                    content
                ], style={"text-align": "left", "padding": "8"})

    return layout


# this is a manually created figure that is used to pass as a default into the following functions
figure_default = {
#             'data': [
#                 go.Scatter(
#                     x=df[df['continent'] == i]['gdp per capita'],
#                     y=df[df['continent'] == i]['life expectancy'],
#                     text=df[df['continent'] == i]['country'],
#                     mode='markers',
#                     opacity=0.7,
#                     marker={
#                         'size': 15,
#                         'line': {'width': 0.5, 'color': 'white'}
#                     },
#                     name=i
#                 ) for i in df.continent.unique()
#             ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
            }


# this function puts a graph into a graph element and enclose that in a div
def graph_content(figure=figure_default, graph_id="graph-content_" + str(round(random() * 10 ** 6))):
    layout = html.Div(
                [
                    dcc.Graph(
                        id=graph_id,
                        figure=figure,
                    )
                ])

    return layout


# # this function puts a graph into a graph element and enclose that in a div
# def graph_content_dyn(control_html=None, graph_id="graph-content_" + str(round(random() * 10 ** 6))):
#     layout = html.Div(
#                 [
#                     dcc.Graph(id=graph_id),
#                     control_html
#                 ])
#
#     return layout