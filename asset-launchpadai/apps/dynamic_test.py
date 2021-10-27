# # -*- coding: utf-8 -*-
# # import json
# # import math

# import pandas as pd
# # import flask
# # import dash
# from dash.dependencies import Input, Output  # can also import "State" if used in app
# import dash_core_components as dcc
# import dash_html_components as html
# # import plotly.plotly as py
# from plotly import graph_objs as go
# from apps import template_obj, chart_template, page_template
# from app import app  # other objects such as "indicator" can be imported and used it

# # data that is used in the the dynamic plot
# df = pd.read_csv('data/indicators.csv')

# # test list that is used in one of the layouts to dynamically generate bullet points
# my_list = ["testing", "one", "two", "three", "..."]

# available_indicators = df['Indicator Name'].unique()

# # manually created content, this is a layout that has a small panel on the left side and a large panel on the right
# # this is here only as an example, there is a dynamically generated version of this below
# layout_left_pan = [

#     # title row
#     html.Div(
#         [
#             html.H3("Lead for the page"),
#         ],
#         className="row",
#         style={
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),

#     # main content row - this is an example of a two column layout with controls on the LHS
#     html.Div(
#         [
#             # controls in the left panel
#             html.Div(
#                 [
#                     html.P("Controls go here"),
#                     html.Div([
#                         dcc.Dropdown(
#                             id='xaxis-column',
#                             options=[{'label': i, 'value': i} for i in available_indicators],
#                             value='Fertility rate, total (births per woman)'
#                         ),
#                         dcc.RadioItems(
#                             id='xaxis-type',
#                             options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                             value='Linear',
#                             labelStyle={'display': 'inline-block'}
#                         )
#                     ], style={'width': '95%', "display": "inline-block", "text-align": "left"}),

#                     html.Div([
#                         dcc.Dropdown(
#                             id='yaxis-column',
#                             options=[{'label': i, 'value': i} for i in available_indicators],
#                             value='Life expectancy at birth, total (years)'
#                         ),
#                         dcc.RadioItems(
#                             id='yaxis-type',
#                             options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                             value='Linear',
#                             labelStyle={'display': 'inline-block'}
#                         )
#                     ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
#                 ],
#                 className="three columns chart_div",
#                 style={"text-align": "center"},
#             ),
#             # main content and chart div - the graph goes in here
#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             html.P("Chart Title here"),
#                             dcc.Graph(id='indicator-graphic'),

#                             dcc.Slider(
#                                 id='year--slider',
#                                 min=df['Year'].min(),
#                                 max=df['Year'].max(),
#                                 value=df['Year'].max(),
#                                 marks={str(year): str(year) for year in df['Year'].unique()}
#                             ),
#                         ], style={'width': '90%', "display": "inline-block", "text-align": "left",
#                                   "marginBottom": "30px"}),
#                 ],
#                 className="nine columns chart_div",
#                 style={"text-align": "center", "height": "100%", "width": "100%"},
#             ),
#         ],
#         className="row",
#         style={"marginTop": "5px", "display": "flex"}
#     ),

#     # table div
#     html.Div(
#         [
#             html.P("Assumptions or other notes about the analysis"),
#         ],
#         className="row",
#         style={
#             "maxHeight": "350px",
#             "overflowY": "scroll",
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),
# ]

# # manually created content, this is a layout that has a small panel on the right side and a large panel in the left
# # this is here only as an example, there is a dynamically generated version of this below
# layout_right_pan = [

#     # title row
#     html.Div(
#         [
#             html.H3("Lead for the page"),
#         ],
#         className="row",
#         style={
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),

#     # main content row - this is an example of a two column layout with controls on the LHS
#     html.Div(
#         [

#             # main content and chart div - the graph goes in here
#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             html.P("Chart Title here"),
#                             dcc.Graph(id='indicator-graphic'),

#                             dcc.Slider(
#                                 id='year--slider',
#                                 min=df['Year'].min(),
#                                 max=df['Year'].max(),
#                                 value=df['Year'].max(),
#                                 marks={str(year): str(year) for year in df['Year'].unique()}
#                             ),
#                         ], style={'width': '90%', "display": "inline-block", "text-align": "left",
#                                   "marginBottom": "30px"}),
#                 ],
#                 className="nine columns chart_div",
#                 style={"text-align": "center", "height": "100%"},
#             ),

#             # controls in the right panel
#             html.Div(
#                 [
#                     html.P("Controls go here"),
#                     html.Div([
#                         dcc.Dropdown(
#                             id='xaxis-column',
#                             options=[{'label': i, 'value': i} for i in available_indicators],
#                             value='Fertility rate, total (births per woman)'
#                         ),
#                         dcc.RadioItems(
#                             id='xaxis-type',
#                             options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                             value='Linear',
#                             labelStyle={'display': 'inline-block'}
#                         )
#                     ], style={'width': '95%', "display": "inline-block", "text-align": "left"}),

#                     html.Div([
#                         dcc.Dropdown(
#                             id='yaxis-column',
#                             options=[{'label': i, 'value': i} for i in available_indicators],
#                             value='Life expectancy at birth, total (years)'
#                         ),
#                         dcc.RadioItems(
#                             id='yaxis-type',
#                             options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                             value='Linear',
#                             labelStyle={'display': 'inline-block'}
#                         )
#                     ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
#                 ],
#                 className="three columns chart_div",
#                 style={"text-align": "center"},
#             ),
#         ],
#         className="row",
#         style={"marginTop": "5px", "display": "flex"}
#     ),

#     # table div
#     html.Div(
#         [
#             html.P("Assumptions or other notes about the analysis"),
#         ],
#         className="row",
#         style={
#             "maxHeight": "350px",
#             "overflowY": "scroll",
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),
# ]

# # manually created content, this is a layout that has a three equally spaced and sized panels this is here only as an
# # example, there is a dynamically generated version of this below
# layout_three_pan = [

#     # title row
#     html.Div(
#         [
#             html.H3("Lead for the page"),
#         ],
#         className="row",
#         style={
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),

#     # main content row - this is an example of a two column layout with controls on the LHS
#     html.Div(
#         [

#             # main content and chart div - the graph goes in here
#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             html.P("Left panel", style={"text-align": "left"}),
#                             html.Ul([
#                                 html.Li('testing'),
#                                 html.Ul([
#                                     html.Li('testing'),
#                                     html.Li('one'),
#                                     html.Li('two'),
#                                     html.Li('three'),
#                                     html.Li('...')
#                                 ]),
#                                 html.Li('one'),
#                                 html.Li('two'),
#                                 html.Li('three'),
#                                 html.Li('...')
#                             ])
#                         ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
#                 ],
#                 className="four columns chart_div",
#                 style={"text-align": "center"},
#             ),

#             html.Div(
#                 [
#                     template_obj.title_textbox(title="Scatter plot of something",
#                                                content=template_obj.graph_content(
#                                                    figure=chart_template.dist_hist_chart()))
#                 ],
#                 className="four columns chart_div",
#                 style={"text-align": "center"},
#             ),

#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             html.P(u'''\
#                                     Right panel: a ac accumsan ad adipiscing aenean aliquam aliquet amet ante aptent 
#                                     auctor augue bibendum blandit class commodo condimentum congue consectetuer
#                                     consequat conubia convallis cras cubilia cum curabitur curae cursus dapibus
#                                     diam dictum dictumst dignissim dis dolor donec dui duis egestas eget eleifend
#                                     elementum elit enim erat eros est et etiam eu euismod facilisi facilisis fames
#                                     faucibus felis fermentum feugiat fringilla fusce gravida habitant habitasse hac
#                                     hendrerit hymenaeos iaculis id imperdiet in inceptos integer interdum ipsum
#                                     justo lacinia lacus laoreet lectus leo libero ligula litora lobortis lorem
#                                     luctus maecenas magna magnis malesuada massa mattis mauris metus mi molestie
#                                     mollis montes morbi mus nam nascetur natoque nec neque netus nibh nisi nisl non
#                                     nonummy nostra nulla nullam nunc odio orci ornare parturient pede pellentesque
#                                     penatibus per pharetra phasellus placerat platea porta porttitor posuere
#                                     potenti praesent pretium primis proin pulvinar purus quam quis quisque rhoncus
#                                     ridiculus risus rutrum sagittis sapien scelerisque sed sem semper senectus sit
#                                     sociis sociosqu sodales sollicitudin suscipit suspendisse taciti tellus tempor
#                                     tempus tincidunt torquent tortor tristique turpis ullamcorper ultrices
#                                     ultricies urna ut varius vehicula vel velit venenatis vestibulum vitae vivamus
#                                     viverra volutpat vulputate'''),
#                         ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
#                 ],
#                 className="four columns chart_div",
#                 style={"text-align": "center"},
#             ),
#         ],
#         className="row",
#         style={"marginTop": "5px", "display": "flex"}
#     ),

#     # table div
#     html.Div(
#         [
#             html.P("Assumptions or other notes about the analysis"),
#         ],
#         className="row",
#         style={
#             "maxHeight": "350px",
#             "overflowY": "scroll",
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),
# ]

# # manually created content, this is a layout that has a two equally spaced and sized panels this is here only as an
# # example, there is a dynamically generated version of this below
# layout_two_pan = [

#     # title row
#     html.Div(
#         [
#             html.H3("Lead for the page"),
#         ],
#         className="row",
#         style={
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),

#     # main content row - this is an example of a two column layout with controls on the LHS
#     html.Div(
#         [

#             # main content and chart div - the graph goes in here
#             html.Div(
#                 [
#                     template_obj.title_textbox(title="Left panel title new",
#                                                content=html.Ul([html.Li(x) for x in my_list]))

#                 ],
#                 className="six columns chart_div",
#                 style={"text-align": "center"},
#             ),
#             html.Div(
#                 [
#                     html.Div(
#                         [
#                             # title row
#                             html.Div(
#                                 [
#                                     html.H5("Right panel title", style={"color": "#FFFFFF", "text-align": "left"}),
#                                 ],
#                                 className="row",
#                                 style={
#                                     "padding": "8",
#                                     "marginBottom": "5",
#                                     "backgroundColor": "#2a3f5f",
#                                     "borderRadius": "0px"
#                                 },
#                             ),
#                             html.Div(
#                                 [
#                                     # html.Ul([html.Li(x) for x in my_list])
#                                     html.P(u'''\
#                                             Right panel: a ac accumsan ad adipiscing aenean aliquam aliquet amet ante 
#                                             auctor augue bibendum blandit class commodo condimentum congue consectetuer
#                                             consequat conubia convallis cras cubilia cum curabitur curae cursus dapibus
#                                             diam dictum dictumst dignissim dis dolor donec dui duis egestas eget 
#                                             elementum elit enim erat eros est et etiam eu euismod facilisi facilisis 
#                                             faucibus felis fermentum feugiat fringilla fusce gravida habitant habitasse
#                                             hendrerit hymenaeos iaculis id imperdiet in inceptos integer interdum ipsum
#                                             justo lacinia lacus laoreet lectus leo libero ligula litora lobortis lorem
#                                             luctus maecenas magna magnis malesuada massa mattis mauris metus mi molestie
#                                             mollis montes morbi mus nam nascetur natoque nec neque netus nibh nisi nisl
#                                             nonummy nostra nulla nullam nunc odio orci ornare parturient pede 
#                                             penatibus per pharetra phasellus placerat platea porta porttitor posuere
#                                             potenti praesent pretium primis proin pulvinar purus quam quis quisque 
#                                             ridiculus risus rutrum sagittis sapien scelerisque sed sem semper senectus 
#                                             sociis sociosqu sodales sollicitudin suscipit suspendisse taciti tellus 
#                                             tempus tincidunt torquent tortor tristique turpis ullamcorper ultrices
#                                             ultricies urna ut varius vehicula vel velit venenatis vestibulum vitae 
#                                             viverra volutpat vulputate''', style={"text-align": "left"}),
#                                 ], style={'width': '95%', "display": "inline-block", "text-align": "left"}),
#                         ]),

#                 ],
#                 className="six columns chart_div",
#                 style={"text-align": "center"},
#             ),
#         ],
#         className="row",
#         style={"marginTop": "5px", "display": "flex"}
#     ),

#     # table div
#     html.Div(
#         [
#             html.P("Assumptions or other notes about the analysis"),
#         ],
#         className="row",
#         style={
#             "maxHeight": "350px",
#             "overflowY": "scroll",
#             "padding": "8",
#             "marginTop": "5",
#             "backgroundColor": "white",
#             "border": "1px solid #C8D4E3",
#             "borderRadius": "3px"
#         },
#     ),
# ]

# # Here is an example of creating an executive summary in a tab. This example uses the layout_single_panel from the
# # page_layout.py file. Note that the content is manually created inside the function call but could be generated
# # outside the call and passed as a variable into the function. Also note to have "selected bold text" the "children"
# # property of the html.Li or html.Ul is used, to create bold text put the text inside of a html.B function as below.
# # The text color for the bold text is set in the CSS file in the assets folder. Finally, to crete a sublist at any
# # point simply add a html.Ul function and add as many "list items" (html.Li) to that function as needed for elements
# # in the sub list
# layout_page_one = page_template.layout_single_panel(page_lead="Executive summary: ",
#                                                     main_panel_content=template_obj.blank_textbox(
#                                                         content=html.Ul([
#                                                             html.Li(children=[html.B('First major point: '),
#                                                                               'description of first major']),
#                                                             html.Ul([
#                                                                 html.Li('First minor point'),
#                                                                 html.Li('Second minor point'),
#                                                                 html.Li('Third minor point')
#                                                             ]),
#                                                             html.Li(children=[html.B('Second major point: '),
#                                                                               'description of second major']),
#                                                             html.Ul([
#                                                                 html.Li('First minor point'),
#                                                                 html.Li('Second minor point')
#                                                             ]),
#                                                             html.Li(children=[html.B('Third major point: '),
#                                                                               'description of third major']),
#                                                             html.Li(children=[html.B('Fourth major point: '),
#                                                                               'description of fourth major']),
#                                                             html.Ul([
#                                                                 html.Li('First minor point'),
#                                                                 html.Li('Second minor point'),
#                                                                 html.Li('Third minor point')
#                                                             ]),
#                                                             html.Li(children=[html.B('Fifth major point'),
#                                                                               'description of fifth major'])
#                                                         ])
#                                                     ),
#                                                     )

# # Manually create the controls that will be passed to the left or right panels in the function calls below
# # The "id" in the drop down menus below are use to pass the value to the call back below. Options are generated from
# # the data in available_indicators, which was loaded from a CSV file above. Value is the default value before the user
# # selects any options
# controls = html.Div(
#     [
#         html.P("Controls go here"),
#         html.Div([
#             dcc.Dropdown(
#                 id='xaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='Fertility rate, total (births per woman)'
#             ),
#             dcc.RadioItems(
#                 id='xaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ], style={'width': '95%', "display": "inline-block", "text-align": "left"}),

#         html.Div([
#             dcc.Dropdown(
#                 id='yaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='Life expectancy at birth, total (years)'
#             ),
#             dcc.RadioItems(
#                 id='yaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ], style={'width': '95%', "display": "inline-block", "text-align": "left"})
#     ])

# # Example of a dynamically generated chart that is connected to controls that were created above. The graph is actually
# # created in the call back below an passed to the dcc.Graph element here using the graph id. Also note that a slider is
# # created that is connected to the chart in the same way as the controls in the panel
# dyn_graph = html.Div(
#     [
#         html.Div(
#             [
#                 html.P("Chart Title here"),
#                 dcc.Graph(id='indicator-graphic'),

#                 dcc.Slider(
#                     id='year--slider',
#                     min=df['Year'].min(),
#                     max=df['Year'].max(),
#                     value=df['Year'].max(),
#                     marks={str(year): str(year) for year in df['Year'].unique()}
#                 ),
#             ], style={'width': '90%', "display": "inline-block", "text-align": "left",
#                       "marginBottom": "30px"}),
#     ],
#     className="nine columns chart_div",
#     style={"text-align": "center", "height": "100%", "width": "100%"},
# )

# # layout_page_two = page_template.layout_right_small(page_lead="Test page lead",
# #                                                    left_panel_content=dyn_graph,
# #                                                    right_panel_content=controls,
# #                                                    )

# layout_page_three = page_template.layout_left_small(page_lead="Test page lead",
#                                                     left_panel_content=controls,
#                                                     right_panel_content=dyn_graph,
#                                                     )

# test = dcc.Markdown('''
# This is a list
# * **Item 1 has bold text** followed by plain text
# * Some Markdown text with _italics_
#   * Item 2a
#   * Item 2b
# ''')

# layout_page_four = page_template.layout_left_small(page_lead="Test page lead",
#                                                    left_panel_content=template_obj.title_textbox(title="New Title",
#                                                                                                  content=test),
#                                                    right_panel_content=template_obj.graph_content(
#                                                        figure=chart_template.dist_hist_chart()),
#                                                    )

# layout_page_five = page_template.layout_right_small(page_lead="Test page lead",
#                                                     left_panel_content=template_obj.graph_content(
#                                                         figure=chart_template.dist_hist_chart()),
#                                                     right_panel_content=template_obj.title_textbox()
#                                                     )

# layout_page_six = page_template.layout_thee_panel(page_lead="Test page lead",
#                                                   left_panel_content=template_obj.title_textbox(),
#                                                   middle_panel_content=template_obj.title_textbox(),
#                                                   right_panel_content=template_obj.title_textbox()
#                                                   )

# layout_page_seven = page_template.layout_two_panel(page_lead="Test page lead",
#                                                    left_panel_content=template_obj.graph_content(
#                                                        figure=chart_template.dist_hist_chart()),
#                                                    right_panel_content=template_obj.title_textbox()
#                                                    )

# layout_page_eight = page_template.layout_four_panel(page_lead="Test page lead",
#                                                     left_panel_content=template_obj.title_textbox(),
#                                                     middle_right_panel_content=template_obj.title_textbox(),
#                                                     middle_left_panel_content=template_obj.title_textbox(),
#                                                     right_panel_content=template_obj.title_textbox()
#                                                     )

# layout_page_nine = page_template.layout_two_row(page_lead="Test page lead",
#                                                 row_one_title="Title for first row",
#                                                 row_one_content="Content for the first row should be here"
#                                                 )

# layout_page_ten = page_template.layout_three_row(page_lead="Test page lead",
#                                                  row_one_title="Title for first row",
#                                                  row_one_content="Content for the first row should be here"
#                                                  )

# layout_page_eleven = page_template.layout_four_row(page_lead="Test page lead",
#                                                    row_one_title="Title for first row",
#                                                    row_one_content="Content for the first row should be here"
#                                                    )

# layout_page_twelve = page_template.layout_five_row(page_lead="Test page lead",
#                                                    row_one_title="Title for first row",
#                                                    row_one_content="Content for the first row should be here"
#                                                    )

# layout_page_thirteen = page_template.layout_six_row(page_lead="Test page lead",
#                                                     row_one_title="Title for first row",
#                                                     row_one_content="Content for the first row should be here"
#                                                     )

# layout_page_fourteen = \
#     page_template.layout_four_row_three_col(page_lead="Test page lead",
#                                             row_one_title="Title for first row",
#                                             row_one_content="Content for the first row should be here",
#                                             row_one_value="Value here"
#                                             )


# # This function is use to select the page layout for each of the tabs from the index.py page, as input it takes a tab
# # id and returns an layout which is basically html. All of the various page layouts are pre-defined in the
# # page_template.py file
# def dyn_content(page_num="tab-1"):
#     if page_num == "tab-1":
#         return layout_page_one
#     elif page_num == "tab-2":
#         return layout_page_one
#     elif page_num == "tab-3":
#         return layout_page_three
#     elif page_num == "tab-4":
#         return layout_page_four
#     elif page_num == "tab-5":
#         return layout_page_five
#     elif page_num == "tab-6":
#         return layout_page_six
#     elif page_num == "tab-7":
#         return layout_page_seven
#     elif page_num == "tab-8":
#         return layout_page_eight
#     elif page_num == "tab-9":
#         return layout_page_nine
#     elif page_num == "tab-10":
#         return layout_page_ten
#     elif page_num == "tab-11":
#         return layout_page_eleven
#     elif page_num == "tab-12":
#         return layout_page_twelve
#     elif page_num == "tab-13":
#         return layout_page_thirteen
#     elif page_num == "tab-14":
#         return layout_page_fourteen
#     else:
#         return layout_left_pan


# # # this is an example callback function, here it is used to connect the graph to controls and generate the graph
# # # based on the values from the controls. Note that the "Input" has all of the variables which are the id names of the
# # # controls above and that the out put is the id name of the graph that is generated. There are several ways to do this,
# # # including using cookies or invisible divs, see the plotly.dash website for more details and examples
# # # Additional call backs like the one below can be created for other dynamic content
# # @app.callback(
# #     Output('indicator-graphic', 'figure'),
# #     [Input('xaxis-column', 'value'),
# #      Input('yaxis-column', 'value'),
# #      Input('xaxis-type', 'value'),
# #      Input('yaxis-type', 'value'),
# #      Input('year--slider', 'value')])
# # def update_graph(xaxis_column_name, yaxis_column_name,
# #                  xaxis_type, yaxis_type,
# #                  year_value):
# #     # get the data for the year using the value from the year slider from the df, which was loaded from a CSV at the
# #     # beginning of the file
# #     dff = df[df['Year'] == year_value]
# #
# #     # create the scatter plot using the data frame and values from the dropdown menus to select the columns for x and y
# #     # axis
# #     data = [go.Scatter(
# #         x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
# #         y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
# #         text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
# #         mode='markers',
# #         marker={
# #             'size': 15,
# #             'opacity': 0.5,
# #             'line': {'width': 0.5, 'color': 'white'}
# #         }
# #     )]
# #
# #     # set the chart layout and connect to the "linear" and "log" radio buttons for the x and y axis
# #     layout = go.Layout(
# #         xaxis={
# #             'title': xaxis_column_name,
# #             'type': 'linear' if xaxis_type == 'Linear' else 'log'
# #         },
# #         yaxis={
# #             'title': yaxis_column_name,
# #             'type': 'linear' if yaxis_type == 'Linear' else 'log'
# #         },
# #         margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
# #         hovermode='closest'
# #     )
# #
# #     # build the figure from the chart and the layout
# #     fig = go.Figure(data=data, layout=layout)
# #
# #     return fig
