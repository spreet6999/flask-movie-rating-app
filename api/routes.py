from flask import Blueprint, jsonify, request
from . import db
from .models import User, Movie
from flask_cors import CORS

main = Blueprint("main", __name__)
CORS(main)


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
