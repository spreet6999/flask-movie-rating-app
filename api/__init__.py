from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy

# print(dir(Flask))
db = SQLAlchemy()
# print(dir(db))


def create_app():
    # this __name__ will point to current file in which it is being called here it is __init__
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app


# if __name__ == "__main__":
#     create_app().run(debug=True)
