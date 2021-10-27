# import required flask modules
from flask import Flask, Blueprint, json, jsonify, request
import pandas as pd
import time
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_cors import CORS
# this __name__ will point to current file in which
# it is being called here it is __init__
app = Flask(__name__)

# getting df
start_time = time.time()
# df = pd.read_json("sales_data.json", orient="records",
#                   convert_dates=True, keep_default_dates=True)
# df = pd.read_json("sales_data.json", orient="records")
df_cleaned_post_update_edit = pd.read_csv("df_cleaned_post_update_edit.csv", index_col=False)
print(df_cleaned_post_update_edit.shape)

end_time = time.time()
duration = round(end_time-start_time, 3)
print(f'df_sales_data read in {duration}')

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

CORS(app)

# if __name__ == "__main__":
#     print("inside if")
#     app.run(debug=True)
