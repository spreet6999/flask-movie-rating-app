import pandas as pd

# * Automating/scripting update_app_edits function from asset-launchpadai/chart_template.py

# ! Keeping the name same as asset-launchpadai code

df_cleaned = pd.read_csv("data/05_model_input/master_dataframe_cln_25K.csv", index_col=False)
print (df_cleaned.shape)
server_data = pd.read_pickle("data/06_model_output/master_dataframe_app_update.pkl")
print (server_data.shape)
for col in server_data['update_col'].unique():
    server_data_mini = server_data[server_data['update_col'] == col]
    for val in server_data_mini['update_val'].unique():
        mat_list = server_data_mini[server_data_mini['update_val'] == val]['Material']
        df_cleaned.loc[df_cleaned['Material'].isin(mat_list), col] = val
print (df_cleaned.shape)
df_cleaned.to_csv("data/poc/df_cleaned_post_update_edit.csv", index=False)