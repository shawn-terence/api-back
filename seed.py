import random
from flask import Flask
from models import db, Movies, MovieInfo, Series, SeriesInfo, Trailer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'
db.init_app(app)

def seed_data():
    with app.app_context():
        
        print("Seeding Movies")