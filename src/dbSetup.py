# import db from app
from app import db

# dropping any existing tables
db.drop_all()

# creating all the tables which are defined in our application
db.create_all()
