from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
# Define set_password, check_password, and generate_token methods


# Define the association table for the many-to-many relationship between User and Movie
user_movie_association = db.Table('user_movie_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    price = db.Column(db.Integer)
    poster = db.Column(db.String(255))
    trailer_url = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(50))

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'description': self.description,
            'rating': self.rating,
            'price': self.price,
            'poster': self.poster,
            'trailer_url': self.trailer_url,
            'genre': self.genre
        }

    fans = db.relationship('User', secondary=user_movie_association, back_populates='movies')


class Ontheatre(db.Model):
    __tablename__ = 'Ontheatre'

    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    runtime = db.Column(db.Integer)
    seats = db.Column(db.String)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    rating_theater = db.Column(db.Float)
    poster_theater = db.Column(db.String(255))
    trailer_url_theater = db.Column(db.String(255), nullable=False)
    genre_theater = db.Column(db.String(50))
    price_theater = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'movie_id': self.movie_id,
            'runtime': self.runtime,
            'seats': self.seats,
            'title': self.title,
            'year': self.year,
            'description': self.description,
            'rating_theater': self.rating_theater,
            'poster_theater': self.poster_theater,
            'trailer_url_theater': self.trailer_url_theater,
            'genre_theater': self.genre_theater,
            'price_theater': self.price_theater
        }


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    gmail = db.Column(db.String)
    password = db.Column(db.String)

    movies = db.relationship('Movies', secondary=user_movie_association, back_populates='fans')

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'gmail': self.gmail,
            'password': self.password
        }

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def generate_token(self):
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)  # Token expiration time
        }
        return jwt.encode(payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')
