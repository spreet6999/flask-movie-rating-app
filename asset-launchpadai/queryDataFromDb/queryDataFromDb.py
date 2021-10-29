# ! Defining required lib
import re
import pandas as pd
import numpy as np
import psycopg2
import math
import re
from flask import jsonify

table_name = "master_dataframe_cln_and_edited"
dbname = "dash_app"
host = "host.docker.internal" #this means "localhost" inside docker
user = "postgres"
password = "1234"
conn = psycopg2.connect(dbname=dbname, user=user,host=host, password=password)

def filter_query_gen(col_val="PTG", col_name="SBU", sql_filter_query=""):
    # ! SQL FILTER QUERY
    if col_val is not None:
        sql_filter_query = f"""{sql_filter_query} "{col_name}" = '{col_val}' AND"""
    return sql_filter_query

def get_pareto_chart_data_from_db(payload):
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
    # * In the below query, category and filters need to be parameterized
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
    cur.close()
    print (type(result))
    print (len(result))
    if len(result) > 0:
        df = pd.DataFrame(result)
        df.columns = col_list
        resp = df.to_dict(orient="records")
        return resp
    else:
        df = pd.DataFrame([('NO DATA', 0.0, 0.0, 0.0, 0, 0)])
        df.columns = col_list
        resp = df.to_dict(orient="records")
        return resp

# This function will bring dropdown values for Level, SBU, SubSBU
def get_pareto_chart_filter_values():
    # df_cleaned_post_update_edit = pd.read_csv("data/poc/df_cleaned_post_update_edit.csv", index_col=False)
    # sbu_data = list(df_cleaned_post_update_edit['SBU'].unique())
    # sub_sbu_data = list(df_cleaned_post_update_edit['SubSBU'].unique())
    cur = conn.cursor()
    sbu_data_query = f"""select DISTINCT "SBU" from master_dataframe_cln_and_edited"""
    cur.execute(sbu_data_query)
    sbu_data = cur.fetchall()
    sbu_data = list(map(lambda x: list(x),sbu_data))
    sbu_data = [item for sublist in sbu_data for item in sublist]

    sub_sbu_data_query = f"""select DISTINCT "SubSBU" from master_dataframe_cln_and_edited"""
    cur.execute(sub_sbu_data_query)
    sub_sbu_data = cur.fetchall()
    sub_sbu_data = list(map(lambda x: list(x),sub_sbu_data))
    sub_sbu_data = [item for sublist in sub_sbu_data for item in sublist]
    cur.close()
    print ("sbu_data", sbu_data)
    print ("sub_sbu_data", sub_sbu_data)
    filters = {"SBU":sbu_data, "SubSBU":sub_sbu_data}
    return filters
