from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db' 

db = SQLAlchemy(app)

# Define the association table for the many-to-many relationship between User and Movie
user_movie_association = db.Table('user_movie_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movies.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    gmail = db.Column(db.String)
    password = db.Column(db.String)

    # Define the relationship with Movie
    favorite_movies = db.relationship('Movie', secondary=user_movie_association, backref='fans')

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'gmail': self.gmail,
            'password': self.password
        }

class Movie(db.Model):
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
        return{
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
        return{
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
