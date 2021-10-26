# import required flask modules
from flask import Flask, Blueprint, json, jsonify, request
from werkzeug.datastructures import _options_header_vkw
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
from flask_cors import CORS

# this __name__ will point to current file in which
# it is being called here it is __init__
app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

CORS(app)


@app.route("/", methods=["GET"])
def exp_route():
    return "Hello World", 200


if __name__ == "__main__":
    app.run(debug=True)
