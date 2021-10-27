# import the libraries used
# import dash_core_components as dcc
import dash_html_components as html


# this function creates a page layout with a single title div and one large panel below
def layout_single_panel(page_lead="Lead for the page",
                        main_panel_content=html.P("Put the content for main panel here")
                        ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(main_panel_content, style={"margin":20},),

                    ],
                    className="twelve columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
    ]

    return layout


# this function creates a page layout with a single title div and two side-by-side panels and that are equally sized
# as well as a single div on the bottom of the page to put assumptions or other notes
def layout_two_panel(page_lead="Lead for the page",
                     left_panel_content=html.P("Put the content for left panel here"),
                     right_panel_content=html.P("Put the content for right panel here"),
                     bottom_content=html.P("Put the content for bottom panel here")
                     ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="six columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="six columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and three side-by-side panels and that are equally sized
# as well as a single div on the bottom of the page to put assumptions or other notes
def layout_thee_panel(page_lead="Lead for the page",
                      left_panel_content=html.P("Put the content for left panel here"),
                      middle_panel_content=html.P("Put the content for left panel here"),
                      right_panel_content=html.P("Put the content for right panel here"),
                      bottom_content=html.P("Put the content for bottom panel here")
                      ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        middle_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and four side-by-side panels and that are equally sized
# as well as a single div on the bottom of the page to put assumptions or other notes
def layout_four_panel(page_lead="Lead for the page",
                      left_panel_content=html.P("Put the content for left panel here"),
                      middle_left_panel_content=html.P("Put the content for middle left panel here"),
                      middle_right_panel_content=html.P("Put the content for middle right panel here"),
                      right_panel_content=html.P("Put the content for right panel here"),
                      bottom_content=html.P("Put the content for bottom panel here")
                      ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        middle_left_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        middle_right_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="four columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and a small panel on the left side and a large panel on
# the right as well as a single div on the bottom of the page to put assumptions or other notes
def layout_left_small(page_lead="Lead for the page",
                      left_panel_content=html.P("Put the content for left panel here"),
                      right_panel_content=html.P("Put the content for right panel here"),
                      bottom_content=html.P("Put the content for bottom panel here")
                      ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="three columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="nine columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and a small panel on the left side and a large panel on
# the right as well as a single div on the bottom of the page to put assumptions or other notes
def layout_left_very_small(page_lead="Lead for the page",
                      left_panel_content=html.P("Put the content for left panel here"),
                      right_panel_content=html.P("Put the content for right panel here"),
                      bottom_content=html.P("Put the content for bottom panel here")
                      ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="one columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="eleven columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and a small panel on the right side and a large panel on
# the left as well as a single div on the bottom of the page to put assumptions or other notes
def layout_right_small(page_lead="Lead for the page",
                       left_panel_content=html.P("Put the content for left panel here"),
                       right_panel_content=html.P("Put the content for right panel here"),
                       bottom_content=html.P("Put the content for bottom panel here")
                       ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        left_panel_content

                    ],
                    className="nine columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        right_panel_content

                    ],
                    className="three columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and two rows that are equal height to each other. In
# each row there are two panels, one smaller on the left that has a colored background. Additionally, there is a single
# div on the bottom of the page to put assumptions or other notes
def layout_two_row(page_lead="Lead for the page",
                   col_one_title="First Col Title",
                   col_two_title="Second Col Title",
                   row_one_title=" Put the title for row 1 here",
                   row_one_content="Put the content for row 1 here",
                   row_two_title="Put the title for row 2 here",
                   row_two_content="Put the content for row 2 here",
                   bottom_content=html.P("Put the content for bottom panel here"),
                   row_height=str((600 - 20) / 2) + "px"
                   ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and three rows that are equal height to each other. In
# each row there are two panels, one smaller on the left that has a colored background. Additionally, there is a single
# div on the bottom of the page to put assumptions or other notes
def layout_three_row(page_lead="Lead for the page",
                     col_one_title="First Col Title",
                     col_two_title="Second Col Title",
                     row_one_title="Put the title for row 1 here",
                     row_one_content="Put the content for row 1 here",
                     row_two_title="Put the title for row 2 here",
                     row_two_content="Put the content for row 2 here",
                     row_three_title="Put the title for row 3 here",
                     row_three_content="Put the content for row 3 here",
                     bottom_content=html.P("Put the content for bottom panel here"),
                     row_height=str((600 - 20) / 3) + "px"
                     ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_three_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_three_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and four rows that are equal height to each other. In
# each row there are two panels, one smaller on the left that has a colored background. Additionally, there is a single
# div on the bottom of the page to put assumptions or other notes
def layout_four_row(page_lead="Lead for the page",
                    col_one_title="First Col Title",
                    col_two_title="Second Col Title",
                    row_one_title="Put the title for row 1 here",
                    row_one_content="Put the content for row 1 here",
                    row_two_title="Put the title for row 2 here",
                    row_two_content="Put the content for row 2 here",
                    row_three_title="Put the title for row 3 here",
                    row_three_content="Put the content for row 3 here",
                    row_four_title="Put the title for row 4 here",
                    row_four_content="Put the content for row 4 here",
                    bottom_content=html.P("Put the content for bottom panel here"),
                    row_height=str((600 - 20) / 4) + "px"
                    ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title, style={"color": "var(--Primary-text)", "padding": "8",
                                                     "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_three_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_three_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_four_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_four_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and five rows that are equal height to each other. In
# each row there are two panels, one smaller on the left that has a colored background. Additionally, there is a single
# div on the bottom of the page to put assumptions or other notes
def layout_five_row(page_lead="Lead for the page",
                    col_one_title="First Col Title",
                    col_two_title="Second Col Title",
                    row_one_title="Put the title for row 1 here",
                    row_one_content="Put the content for row 1 here",
                    row_two_title="Put the title for row 2 here",
                    row_two_content="Put the content for row 2 here",
                    row_three_title="Put the title for row 3 here",
                    row_three_content="Put the content for row 3 here",
                    row_four_title="Put the title for row 3 here",
                    row_four_content="Put the content for row 4 here",
                    row_five_title="Put the title for row 5 here",
                    row_five_content="Put the content for row 5 here",
                    bottom_content=html.P("Put the content for bottom panel here"),
                    row_height=str((600 - 20) / 5) + "px"
                    ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_three_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_three_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_four_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_four_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_five_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_five_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and six rows that are equal height to each other. In
# each row there are two panels, one smaller on the left that has a colored background. Additionally, there is a single
# div on the bottom of the page to put assumptions or other notes
def layout_six_row(page_lead="Lead for the page",
                   col_one_title="First Col Title",
                   col_two_title="Second Col Title",
                   row_one_title="Put the title for row 1 here",
                   row_one_content="Put the content for row 1 here",
                   row_two_title="Put the title for row 2 here",
                   row_two_content="Put the content for row 2 here",
                   row_three_title="Put the title for row 3 here",
                   row_three_content="Put the content for row 3 here",
                   row_four_title="Put the title for row 3 here",
                   row_four_content="Put the content for row 4 here",
                   row_five_title="Put the title for row 5 here",
                   row_five_content="Put the content for row 5 here",
                   row_six_title="Put the title for row 6 here",
                   row_six_content="Put the content for row 6 here",
                   bottom_content=html.P("Put the content for bottom panel here"),
                   row_height=str((600 - 20) / 6) + "px"
                   ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_three_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_three_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_four_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_four_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_five_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_five_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_six_title, style={"color": "var(--Primary-text)", "padding": "8",
                                                     "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_six_content, style={"padding": "8"})

                    ],
                    className="ten columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout


# this function creates a page layout with a single title div and four rows that are equal height to each other. In
# each row there are three, one smaller on the left that has a colored background, the second is large in the middle
# the third is small on the right to contain a value. Additionally, there is a single div on the bottom of the page
# to put assumptions or other notes
def layout_four_row_three_col(page_lead="Lead for the page",
                              col_one_title="First Col Title",
                              col_two_title="Second Col Title",
                              col_three_title="Third Col Title",
                              row_one_title="Put the title for row 1 here",
                              row_one_content="Put the content for row 1 here",
                              row_one_value="Put the value for row 1 here",
                              row_two_title="Put the title for row 2 here",
                              row_two_content="Put the content for row 2 here",
                              row_two_value="Put the value for row 2 here",
                              row_three_title="Put the title for row 3 here",
                              row_three_content="Put the content for row 3 here",
                              row_three_value="Put the value for row 3 here",
                              row_four_title="Put the title for row 4 here",
                              row_four_content="Put the content for row 4 here",
                              row_four_value="Put the value for row 4 here",
                              bottom_content=html.P("Put the content for bottom panel here"),
                              row_height=str((600 - 20) / 4) + "px"
                              ):
    layout = [
        # title row
        html.Div(
            [
                html.H3(page_lead),
            ],
            className="row",
            style={
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),

        # Title columns for each of the two columns. Embedding html.B and html.U makes the text bold and underlined.
        # Remove those div's to unbold or remove underline
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.P(html.B(html.U(col_one_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_two_title)), style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="eight columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.P(html.B(html.U(col_three_title)),
                               style={"padding": "8", "margin-bottom": "0"})

                    ],
                    className="two columns chart_div",
                    style={"display": "table"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # main content row - this is an example of a two column layout with controls on the LHS
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_one_title, style={"color": "var(--Primary-text)", "padding": "8",
                                                     "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_one_content, style={"padding": "8"})

                    ],
                    className="eight columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.P(row_one_value,
                               style={"padding": "8", "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),
        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_two_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_two_content, style={"padding": "8"})

                    ],
                    className="eight columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.P(row_two_value,
                               style={"padding": "8", "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_three_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_three_content, style={"padding": "8"})

                    ],
                    className="eight columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.P(row_three_value,
                               style={"padding": "8", "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        html.Div(
            [

                # main content and chart div - the graph goes in here
                html.Div(
                    [
                        html.H4(row_four_title,
                               style={"color": "var(--Primary-text)", "padding": "8", "display": "table-cell",
                                      "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center", "height": row_height, "backgroundColor": "var(--Primary-background)",
                           "display": "table"},
                ),
                html.Div(
                    [
                        html.P(row_four_content, style={"padding": "8"})

                    ],
                    className="eight columns chart_div",
                    style={"text-align": "center"},
                ),
                html.Div(
                    [
                        html.P(row_four_value,
                               style={"padding": "8", "display": "table-cell", "vertical-align": "middle"})

                    ],
                    className="two columns chart_div",
                    style={"text-align": "center"},
                ),
            ],
            className="row",
            style={"marginTop": "5px", "display": "flex"}
        ),

        # table div
        html.Div(
            [
                bottom_content
            ],
            className="row",
            style={
                "maxHeight": "350px",
                "overflowY": "scroll",
                "padding": "8",
                "marginTop": "5",
                "backgroundColor": "white",
                "border": "1px solid #C8D4E3",
                "borderRadius": "3px"
            },
        ),
    ]

    return layout
