
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

# ! Read tables
# df_cleaned = pd.read_csv("master_dataframe_cln_25K.csv")
df_cleaned = pd.read_csv("df_cleaned_post_update_edit.csv")
print(df_cleaned.shape)
dtype_mapper = {"<class 'str'>": "VARCHAR(8000)", "<class 'float'>": "DOUBLE PRECISION"}
py_dtype_mapper = {"VARCHAR(8000)": "str", "DOUBLE PRECISION": "float"}
dtype_dict_df_cleaned = get_datatypes(df_cleaned)
dtypes_df = pd.DataFrame.from_dict(dtype_dict_df_cleaned, orient="index", columns=["sql_datatype"]).reset_index()
dtypes_df.rename(columns={"index": "column_name"}, inplace=True)
dtypes_df.to_csv("dtypes_for_SQL_tables.csv")
df_types_for_table_cols = pd.read_csv("dtypes_for_SQL_tables.csv")

# ! Cursor
conn = psycopg2.connect(dbname="dash_app", user="postgres",host="localhost", password="1234")
cur = conn.cursor()

# ! Drop and create tables: create_db_tables
delete_query_string = "DROP TABLE IF EXISTS master_dataframe_cln;"
query_string = "CREATE TABLE master_dataframe_cln("
for index, row in df_types_for_table_cols.iterrows():
    subquery_string = f'"{row["column_name"]}" {row["sql_datatype"]}'
    comma_sep = ","
    if index == 0:
        comma_sep = ""
        query_string = query_string + "\n" + subquery_string
    else:
        query_string = query_string + comma_sep + "\n" + subquery_string
query_string = query_string + " );"
#     print(query_string)
cur.execute(delete_query_string)
cur.execute(query_string)
conn.commit()
# def create_db_tables(df_types_for_table_cols):
 

# ! Insert data into tables
# def insert_data_in_db(df_data):
column_name = dtype_dict_df_cleaned.keys()
query_string = "INSERT INTO master_dataframe_cln"
subquery_string = "("

counter = 0
for i in column_name:
    subquery_string = subquery_string + f'"{i}", '
    counter = counter + 1
print ("counter", counter)
subquery_string = re.sub(", $", "", subquery_string)
query_string = query_string + subquery_string + ")"

for index, row in df_cleaned.iterrows():
    print("At index: ", index)
#         query_string = f'INSERT INTO master_dataframe_cln(Material) VALUES("GHYUF67")'
    entries_helper = ""
    entries_query=""
    entries = []
    for i in column_name:
        value = row[i]

        sql_dtype = dtype_dict_df_cleaned[i]
        py_dtype = py_dtype_mapper[sql_dtype]

        final_value = value
        final_value_str = ""
        if py_dtype == "str":
            final_value = str(value)
#                 final_value = "SampleText"
            if isinstance(final_value,str):
                if final_value == "nan":
                    final_value = "EMPTY VALUE"
            final_value= re.sub('''['"]+''', '', final_value)
            final_value_str = f"""'{final_value}'"""
        if py_dtype == "float":
            final_value = float(value)
#                 final_value = 1.0
            if isinstance(final_value,float):
                if math.isnan(final_value):
                    final_value = 0
            final_value_str = f'{final_value}'

#             if isinstance(final_value,float):
#                 if math.isnan(final_value):
#                     final_value = 0
        
#             if isinstance(final_value,str):
#                 if final_value == "nan":
#                     final_value = "EMPTY VALUE"
                
        entries.append(final_value)
        entries_helper = entries_helper + "%s,"
        entries_query = entries_query + final_value_str + ","

    entries_helper = re.sub(",$", "", entries_helper)
    entries_query = re.sub(",$", "", entries_query)
    print(len(entries))

    per_s_len = len(re.findall("%s", entries_helper))
    print(per_s_len)
    entries = tuple(entries)
#         print(entries)

#         final_query = f'{query_string} VALUES({entries_helper});'
    final_query = f'{query_string} VALUES({entries_query});'
#         print(final_query)

#         print(final_query)
    print("\n##############\n")
#         print(entries)

#         cur.execute(final_query)
#         return entries
#         print(final_query)
    print ("\n")
#         print(entries)
#         return entries
#         final_query = cur.mogrify(final_query, entries)
#         print(final_query)
    cur.execute(final_query)
#         cur.execute(final_query, entries)
    conn.commit()
        
        
