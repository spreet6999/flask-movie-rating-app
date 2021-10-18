from flask import Blueprint, jsonify, request
from . import db
from .models import Movie
from flask_cors import CORS

main = Blueprint("main", __name__)
CORS(main)


@main.route("/api/v1/movies", methods=["GET"])
def get_movies():

    if request.method == "GET":
        movie_list = Movie.query.all()  # SQLite query method to query the db
        movies = []

        for movie in movie_list:
            movies.append({"title": movie.title, "rating": movie.rating})

        return jsonify({"movies": movies})


@main.route("/api/v1/movie", methods=["POST", "GET"])
def movie():

    if request.method == "POST":

        # getting data coming in our request body
        movie_data = request.get_json()
        print(type(movie_data), dir(movie_data))

        try:
            # CHECKING IF MOVIE DATA IS VALID OR NOT
            if movie_data and ("title" in movie_data) and ("rating" in movie_data):
                new_movie = Movie(
                    title=movie_data["title"], rating=movie_data["rating"])

                # CHECKING IF MOVIE ALREADY EXISTS
                doesExists = db.session.query(Movie.query.filter(
                    Movie.title == new_movie.title).exists()).scalar()
                if doesExists:
                    return "Movie already exists!", 422

                # ADDING NEWLY CREATED MOVIE TO OUR DB
                db.session.add(new_movie)
                db.session.commit()

                return "Successfully Added A Movie", 200

            else:
                raise Exception(
                    "Bad request error!, please check your request body")

        except Exception as ex:
            return str(ex), 400
