from app import df_cleaned_post_update_edit
import re
import pandas as pd

table_name = ""
hard_coded_data = pd.read_csv("final_pareto_chart.csv")

def filter_query_gen(col_val="PTG", col_name="SBU", sql_filter_query=""):
    # ! SQL FILTER QUERY
    if col_val is not None:
        sql_filter_query = f"{sql_filter_query} {col_name} = {col_val} AND"
    return sql_filter_query

def get_pareto_chart_data_from_db(payload):
    # TODO SQL QUERY
    user_filters = payload["filters"]
    sbu_filter_val = user_filters["SBU"]
    sub_sbu_filter_val = user_filters["SubSBU"]
    sql_filter_query = "WHERE"
    sql_filter_query = filter_query_gen(col_val=sbu_filter_val, col_name="SBU", sql_filter_query="")
    sql_filter_query = filter_query_gen(col_val=sub_sbu_filter_val, col_name="SubSBU", sql_filter_query=sql_filter_query)
    print ("sql_filter_query", sql_filter_query)
    sql_filter_query = f"WHERE {sql_filter_query}" if sql_filter_query != "" else ""
    # Remove last AND
    sql_filter_query = re.sub("AND$", "", sql_filter_query) 
    # TODO In the below query, category and filters need to be parameterized
    sql_final_query = f"""SELECT 
                        'Category',
                        SUM('Gbl Prev 12Mo GSV $') as 'Gbl Prev 12Mo GSV $', 
                        SUM('Gbl Prev 12Mo Qty') as 'Gbl Prev 12Mo Qty',
                        SUM('Gbl Prev 12Mo Margin ($)') as 'Gbl Prev 12Mo Margin ($)',
                        COUNT DISTINCT('Material') as 'Material', 
                        COUNT DISTINCT('Material_base') as 'Material_base'
                        {sql_filter_query}
                        GROUP BY 'Category'
                        ORDER BY 'Gbl Prev 12Mo GSV $' DESC
                        FROM {table_name}"""
    print ("sql_final_query", sql_final_query)
    resp = hard_coded_data.to_json(orient="records")
    return resp

# This function will bring dropdown values for Level, SBU, SubSBU
def get_pareto_chart_filter_values():
    # TODO SQL QUERY
    sbu_data = list(df_cleaned_post_update_edit['SBU'].unique())
    sub_sbu_data = list(df_cleaned_post_update_edit['SubSBU'].unique())
    filters = {"SBU":sbu_data, "SubSBU":sub_sbu_data}
    return filters
