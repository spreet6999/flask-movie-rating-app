# ! Defining required lib
import re
import pandas as pd
import psycopg2
import math
from app import df_cleaned_post_update_edit
import re
import pandas as pd
from flask import jsonify

table_name = "master_dataframe_cln_and_edited"
# hard_coded_data = pd.read_csv("final_pareto_chart.csv")
conn = psycopg2.connect(dbname="dash_app", user="postgres",host="localhost", password="1234")

def filter_query_gen(col_val="PTG", col_name="SBU", sql_filter_query=""):
    # ! SQL FILTER QUERY
    if col_val is not None:
        sql_filter_query = f"""{sql_filter_query} "{col_name}" = '{col_val}' AND"""
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
                        "Category",
                        SUM("Gbl Prev 12Mo GSV $") as "Gbl Prev 12Mo GSV $", 
                        SUM("Gbl Prev 12Mo Qty") as "Gbl Prev 12Mo Qty",
                        SUM("Gbl Prev 12Mo Margin ($)") as "Gbl Prev 12Mo Margin ($)",
                        COUNT (DISTINCT "Material") as "Material", 
                        COUNT (DISTINCT "Material_base") as "Material_base"
                        FROM {table_name}
                        {sql_filter_query}
                        GROUP BY "Category"
                        ORDER BY "Gbl Prev 12Mo GSV $" DESC;"""
    print ("sql_final_query", sql_final_query)
    cur = conn.cursor()
    col_list = ["Category","Gbl Prev 12Mo GSV $", "Gbl Prev 12Mo Qty","Gbl Prev 12Mo Margin ($)", "Material","Material_base"]
    cur.execute(sql_final_query)
    result = cur.fetchall()
    print (type(result))
    print (len(result))
    if len(result) > 0:
        df = pd.DataFrame(result)
        df.columns = col_list
        cur.close()
        resp = df.to_json(orient="records")
        return resp
    else:
        return jsonify([])

# This function will bring dropdown values for Level, SBU, SubSBU
def get_pareto_chart_filter_values():
    # TODO SQL QUERY
    sbu_data = list(df_cleaned_post_update_edit['SBU'].unique())
    sub_sbu_data = list(df_cleaned_post_update_edit['SubSBU'].unique())
    filters = {"SBU":sbu_data, "SubSBU":sub_sbu_data}
    return filters
