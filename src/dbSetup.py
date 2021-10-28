
# ! Defining required lib
import re
import pandas as pd
import psycopg2
import math

# ! Defining required functions
def get_datatypes(df):
    dtype_dict = {}

    for k in df:
        python_datatype_list = df[k].map(lambda x: type(x))
        python_datatype_list = list(set(python_datatype_list))
        sql_datatype = dtype_mapper[str(python_datatype_list[0])]
        dtype_dict[k] = sql_datatype
    return dtype_dict

# ! Defining required mappers
dtype_mapper = {"<class 'str'>": "VARCHAR(8000)", "<class 'float'>": "DOUBLE PRECISION"}
py_dtype_mapper = {"VARCHAR(8000)": "str", "DOUBLE PRECISION": "float"}

# ! Manipulate dataframe
# READ DF
# df_name = "master_dataframe_cln_25K.csv"
df_name = "df_cleaned_post_update_edit.csv"
df_cleaned = pd.read_csv(df_name, index_col=False)

# THIS NEEDS TO BE DONE FOR DF
dtype_dict_df_cleaned = get_datatypes(df_cleaned)
# Add sql_datatype
dtypes_df = pd.DataFrame.from_dict(dtype_dict_df_cleaned, orient="index", columns=["sql_datatype"]).reset_index()
dtypes_df.rename(columns={"index": "column_name"}, inplace=True)
# Add py_datatype
dtypes_df["py_datatype"] = dtypes_df["sql_datatype"].apply(lambda x: py_dtype_mapper[x])
dtypes_df.to_csv("dtypes_for_SQL_tables.csv", index=False)

# ONCE DONE, WE CAN JUST READ THIS DF
dtypes_df = pd.read_csv("dtypes_for_SQL_tables.csv")
print ("dtypes_df", dtypes_df.shape)
# dtypes_df.head(20)

# Correct dtypes for all columns in main df to match the SQL table schema
col_list = df_cleaned.columns
entries_helper_list = []
for col_name in col_list:
    dtypes_df_subset = dtypes_df[dtypes_df["column_name"] == col_name]
    py_datatype_col = list(dtypes_df_subset["py_datatype"])
    py_datatype = py_datatype_col[0]
    if py_datatype == "str":
        df_cleaned[col_name] = df_cleaned[col_name].astype(str)
    if py_datatype == "float":
        df_cleaned[col_name] = df_cleaned[col_name].astype(float)
        # convert nan to 0.0
        df_cleaned[col_name] = df_cleaned[col_name].apply(lambda x: 0.0 if math.isnan(x) else x)
col_list_len = len(col_list)
entries_helper = list(map(lambda x: "%s",range(col_list_len)))

# ! Make query
table_name = "master_dataframe_cln_and_edited"
delete_query_string = f"DROP TABLE IF EXISTS {table_name};"
create_table_query = f"CREATE TABLE {table_name}("
for index, row in dtypes_df.iterrows():
    subquery_string = f'"{row["column_name"]}" {row["sql_datatype"]}'
    create_table_query = create_table_query + "\n" + subquery_string + ","
#     comma_sep = ","
#     if index == 0:
#         comma_sep = ""
#         create_table_query = create_table_query + "\n" + subquery_string
#     else:
create_table_query = re.sub(",$", "", create_table_query)
create_table_query = create_table_query + ");"
print ("delete_query_string", delete_query_string)
print ("create_table_query", create_table_query)

entries_helper_text = ", ".join(entries_helper)
# Add double quotes to each column name
col_list_with_double_quotes = list(map(lambda x: f'"{x}"', col_list))
# Replace % with %% in column name
# REF: https://stackoverflow.com/questions/29932970/updating-table-with-percent-sign-in-column-name
col_list_with_percent_replaced = list(map(lambda x: x.replace("%", "%%"), col_list_with_double_quotes))
col_names_query = ", ".join(col_list_with_percent_replaced)
insert_data_query = f"INSERT INTO {table_name}({col_names_query}) VALUES ({entries_helper_text})"
print ("insert_data_query", insert_data_query)
 
# ! Make df_cleaned as table
# Execute query to load data to tables
df_cleaned_as_list_of_tuples = list(map(lambda _list: tuple(_list), df_cleaned.values))

# ! Connect to postgresql and run query
conn = psycopg2.connect(dbname="dash_app", user="postgres",host="localhost", password="1234")
cur = conn.cursor()
cur.execute(delete_query_string)
cur.execute(create_table_query)
cur.executemany(insert_data_query, df_cleaned_as_list_of_tuples)
conn.commit()
cur.close()
