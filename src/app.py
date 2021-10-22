# import required flask modules
from flask import Flask, Blueprint, jsonify, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

# this __name__ will point to current file in which
# it is being called here it is __init__
app = Flask(__name__)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "False"


main = Blueprint("main", __name__)
CORS(main)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(128), unique=True, nullable=False)

    # This is a relationship not a column
    movies = db.relationship("Movie", backref="author", lazy=True)

    def __repr__(self):
        return f"User(Full_name: {self.full_name}  ,Username: {self.username}, Email: {self.email})"


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Movie(title: {self.title}, rating: {self.rating}, author_id: {self.author_id})"


def validateRegisterUserData(userData={}):
    print(userData)
    return True


def validateLoginUserData(userData={}):
    print(userData)
    return True


@main.route("/api/v1/movies", methods=["GET"])
def get_movies():
    if request.method == "GET":
        movie_list = Movie.query.all()  # SQLite query method to query the db
        movies = []
        # print(movie_list.id)

        for movie in movie_list:
            print(movie.id, movie.author_id)
            author = User.query.filter(
                User.id == movie.author_id).first_or_404()
            print(author)
            author_name = author.full_name
            movies.append(
                {"title": movie.title, "rating": movie.rating, "author": author_name})

        return jsonify({"movies": movies}), 200


@main.route("/api/v1/movie", methods=["POST", "GET"])
def movie():
    # print(dir(request))
    if request.method == "POST":

        # getting data coming in our request body
        movie_data = request.get_json()
        print(movie_data)
        # print(type(movie_data), dir(movie_data))

        try:
            # CHECKING IF MOVIE DATA IS VALID OR NOT
            if movie_data and ("title" in movie_data) and ("rating" in movie_data):
                new_movie = Movie(
                    title=movie_data["title"], rating=movie_data["rating"])

                # CHECKING IF MOVIE ALREADY EXISTS
                doesExists = db.session.query(Movie.query.filter(
                    Movie.title == new_movie.title).exists()).scalar()
                if doesExists:
                    return jsonify({"message": "Movie already exists!"}), 409

                # ADDING NEWLY CREATED MOVIE TO OUR DB
                db.session.add(new_movie)
                db.session.commit()
                return jsonify({"message": "Successfully Added A Movie"}), 200

            else:
                raise Exception(
                    "Bad request error!, please check your request body")

        except Exception as ex:
            return jsonify({"message": str(ex)}), 400


@main.route("/register", methods=['POST'])
def register():
    user_data = request.get_json()
    if validateRegisterUserData(user_data):
        hashed_password = bcrypt.generate_password_hash(
            user_data.data.password).decode('utf-8')
        user = User(username=user_data.data.username,
                    email=user_data.data.email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": 'Your account has been created! You are now able to log in'}), 200
    return jsonify({"message": "Please check your entries!"}), 401


@main.route("/login", methods=['GET', 'POST'])
def login():
    user_data = request.get_json()

    if (validateLoginUserData(user_data)):
        user = User.query.filter_by(email=user_data.email.data).first()
        if user and bcrypt.check_password_hash(user.password, user_data.password.data):
            return jsonify({"message": "Successfully logged In!"}), 200
        else:
            return jsonify({"message": 'Login Unsuccessful. Please check email or password'}), 401
    return jsonify({"message": "Please check your entries!"}), 401


@main.route("/logout")
def logout():
    # logic here!
    return jsonify({"message": "Successfully logged out!"}), 200


app.register_blueprint(main)


if __name__ == "__main__":
    app.run(debug=True)
