from flask import jsonify, request
from app import app
import time
from dataFromSql import get_pareto_chart_data_from_db, get_pareto_chart_filter_values
import requests
import pandas as pd

response = requests.get('https://run.mocky.io/v3/3a6fd8b3-f154-459f-923b-20010d99e97b')
json = response.json()
df_temp = pd.DataFrame.from_dict(json)

# API to get data for paretoChartData
# This will be a POST call since it will have filters
@app.route("/pareto_chart_data", methods=["POST"])
def pareto_chart_data():
    json = request.get_json()
    print ("JSON", json)
    resp = get_pareto_chart_data_from_db(json)
    return resp, 200

@app.route("/pareto_chart_filter_values", methods=["GET"])
def pareto_chart_filter_values():
    resp = get_pareto_chart_filter_values()
    return jsonify(resp), 200


if __name__ == "__main__":
    print("inside index.py if")
    app.run(debug=True, port="9999")
