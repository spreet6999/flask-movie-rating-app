from . import db


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
