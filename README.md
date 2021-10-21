# flask-movie-rating-app

## After cloning this project

## make sure you have pipenv installed (pip/pip3 install pipenv)

## then run "pipenv shell" to activate virtual environment

## then run pipenv install

## then we have to set environment variables to run the flask app, to do so please follow the below commands:

## export FLASK_APP=api

## export FLASK_ENV=development

## flask run

## this will run your flask application

## you will get local host address in your terminal ex: Running on http://127.0.0.1:5000/

## Now setup your database with database tables structure, to do so please follow the below commands:

## make sure you have deleted any pre-existing database.db file and you are inside the root pipenv folder and pipenv is active (virtual environment is active)

## python3 (you will dive into python interpreter)

## from api.models import Movie

## form api import db, create_app

## db.create_all(app=create_app())

## for other db methods you have to push an application context to your current app

## app = create_app()

## app.app_context().push()

## this will create a dabase.db file inside you root api folder

## you can now consume these apis

## happy coding 😃
