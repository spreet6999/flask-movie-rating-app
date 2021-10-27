# start with some imports--------------------------------------------------------------------------------------------
from apps import chart_template, page_template
from app import df_bom, df_cleaned  # other objects such as "indicator" can be imported and used it
import numpy as np

# function to build the graph and control content -------------------------------------------------------------------
controls, fig = chart_template.create_bom_table(data=df_bom,
                                                master_data=df_cleaned,
                                                filter_col='Material',
                                                filter_col_2='Segment 1',
                                                filter_col_3='Grouping',
                                                filter_col_4='Brand',
                                                filter_col_5='Region'
                                                )

# put the figures into a page layout -------------------------------------------------------------------------------
# put everything into the layout
layout = page_template.layout_right_small(page_lead="BOM Comparison:",
                                          left_panel_content=fig,
                                          right_panel_content=controls
                                          )
