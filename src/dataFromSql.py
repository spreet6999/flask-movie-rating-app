from app import df_cleaned_post_update_edit
import re

table_name = ""

def filter_query_gen(col_val="PTG", col_name="SBU", sql_filter_query=""):
    # ! SQL FILTER QUERY
    sql_query = ""
    if col_val is not None:
        sql_query = f"{sql_query} {col_name} = {col_val} AND"
    return sql_query

def get_pareto_chart_data_from_db(payload):
    # TODO SQL QUERY
    user_filters = payload["filters"]
    sbu_filter_val = user_filters["SBU"]
    sub_sbu_filter_val = user_filters["SubSBU"]
    sql_filter_query = filter_query_gen(col_val=sbu_filter_val, col_name="SBU", sql_filter_query="")
    sql_filter_query = filter_query_gen(col_val=sub_sbu_filter_val, col_name="SubSBU", sql_filter_query="")
    print ("sql_filter_query", sql_filter_query)
    # Remove last AND
    sql_filter_query = re.replace("AND$", "") 
    sql_final_query = f"""SELECT 
                        'Category',
                        SUM('Gbl Prev 12Mo GSV $') as 'Gbl Prev 12Mo GSV $', 
                        SUM('Gbl Prev 12Mo Qty') as 'Gbl Prev 12Mo Qty',
                        SUM('Gbl Prev 12Mo Margin ($)') as 'Gbl Prev 12Mo Margin ($)',
                        COUNT DISTINCT('Material') as 'Material', 
                        COUNT DISTINCT('Material_base') as 'Material_base', 
                        
                        WHERE 
                        {sql_filter_query}

                        GROUP BY 'Category'
                        FROM {table_name}"""
    print ("sql_filter_query", sql_filter_query)
    resp = df_cleaned_post_update_edit.head(10).to_json(orient="records")
    return resp

# This function will bring dropdown values for Level, SBU, SubSBU
def get_pareto_chart_filter_values():
    # TODO SQL QUERY
    sbu_data = list(df_cleaned_post_update_edit['SBU'].unique())
    sub_sbu_data = list(df_cleaned_post_update_edit['SubSBU'].unique())
    filters = {"SBU":sbu_data, "SubSBU":sub_sbu_data}
    return filters
