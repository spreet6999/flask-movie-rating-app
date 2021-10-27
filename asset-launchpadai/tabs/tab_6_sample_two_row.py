# -*- coding: utf-8 -*-
# import json
# import math

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

row_1_content = html.P(u'''Right panel: a ac accumsan ad adipiscing aenean aliquam aliquet amet ante aptent 
                                    auctor augue bibendum blandit class commodo condimentum congue consectetuer
                                    consequat conubia convallis cras cubilia cum curabitur curae cursus dapibus
                                    diam dictum dictumst dignissim dis dolor donec dui duis egestas eget eleifend
                                    elementum elit enim erat eros est et etiam eu euismod facilisi facilisis fames
                                    faucibus felis fermentum feugiat fringilla fusce gravida habitant habitasse hac
                                    hendrerit hymenaeos iaculis id imperdiet in inceptos integer interdum ipsum
                                    justo lacinia lacus laoreet lectus leo libero ligula litora lobortis lorem
                                    luctus maecenas magna magnis malesuada massa mattis mauris metus mi molestie
                                    mollis montes morbi mus nam nascetur natoque nec neque netus nibh nisi nisl non
                                    nonummy nostra nulla nullam nunc odio orci ornare parturient pede pellentesque
                                    penatibus per pharetra phasellus placerat platea porta porttitor posuere
                                    potenti praesent pretium primis proin pulvinar purus quam quis quisque rhoncus
                                    ridiculus risus rutrum sagittis sapien scelerisque sed sem semper senectus sit
                                    sociis sociosqu sodales sollicitudin suscipit suspendisse taciti tellus tempor
                                    tempus tincidunt torquent tortor tristique turpis ullamcorper ultrices
                                    ultricies urna ut varius vehicula vel velit venenatis vestibulum vitae vivamus
                                    viverra volutpat vulputate''')

row_2_content = html.P(u'''Right panel: a ac accumsan ad adipiscing aenean aliquam aliquet amet ante aptent 
                                    auctor augue bibendum blandit class commodo condimentum congue consectetuer
                                    consequat conubia convallis cras cubilia cum curabitur curae cursus dapibus
                                    diam dictum dictumst dignissim dis dolor donec dui duis egestas eget eleifend
                                    elementum elit enim erat eros est et etiam eu euismod facilisi facilisis fames
                                    faucibus felis fermentum feugiat fringilla fusce gravida habitant habitasse hac
                                    hendrerit hymenaeos iaculis id imperdiet in inceptos integer interdum ipsum
                                    justo lacinia lacus laoreet lectus leo libero ligula litora lobortis lorem
                                    luctus maecenas magna magnis malesuada massa mattis mauris metus mi molestie
                                    mollis montes morbi mus nam nascetur natoque nec neque netus nibh nisi nisl non
                                    nonummy nostra nulla nullam nunc odio orci ornare parturient pede pellentesque
                                    penatibus per pharetra phasellus placerat platea porta porttitor posuere
                                    potenti praesent pretium primis proin pulvinar purus quam quis quisque rhoncus
                                    ridiculus risus rutrum sagittis sapien scelerisque sed sem semper senectus sit
                                    sociis sociosqu sodales sollicitudin suscipit suspendisse taciti tellus tempor
                                    tempus tincidunt torquent tortor tristique turpis ullamcorper ultrices
                                    ultricies urna ut varius vehicula vel velit venenatis vestibulum vitae vivamus
                                    viverra volutpat vulputate''')

layout = page_template.layout_two_row(page_lead="Test page lead",
                                      row_one_title="Title for first row",
                                      row_one_content=row_1_content,
                                      row_two_content=row_2_content
                                      )
