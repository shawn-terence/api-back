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

class Ontheatre (db.Model):
    __tablename__ = 'Ontheatre'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    poster = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    trailer_url = db.Column(db.String(255), nullable=False)
    runtime = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    price = db.Column(db.Integer)
    seats = db.Column(db.String)
 
   

    def serialize(self):
        return{
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'description': self.description,
            'rating': self.rating,
            'poster': self.poster,
            'rating': self.rating,
            'trailer_url': self.trailer_url,
            'runtime': self.runtime,
            'genre': self.genre,
            'seats': self.seats,
            'price': self.price
            }
    
            # You can include other attributes from Movie if needed
        
