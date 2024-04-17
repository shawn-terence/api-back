import random
from flask import Flask
from models import db, Movies, User, Ontheatre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'
db.init_app(app)

def seed_data():
    with app.app_context():

        print("Seeding Movies")

        movies_data = [
            {"title": "The Amazing Spider-Man", "year": 2014, "description": "After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to save the city from the machinations of a mysterious reptilian foe.", "rating": 7.5, "price": 700, "poster": "https://i.pinimg.com/564x/c5/7e/b6/c57eb61ecc25097a4a3682238efe3d5d.jpg", "video_url": "https://youtu.be/-tnxzJ0SSOw?si=5KIJncsQKKggyzxM", "genre": "Action"},
            {"title": "Fast and Furious 6", "year": 2013, "description": "Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets sidetracked with facing his presumed deceased girlfriend, Letty.", "rating": 6.7, "price": 500, "poster": "https://i.pinimg.com/564x/19/2a/66/192a66022855d80ea8f95c930382f914.jpg", "video_url": "https://youtu.be/oc_P11PNvRs?si=ObjTbpV4KFohk7NP", "genre": "Action"},
            {"title": "Avengers: Infinity War", "year": 2018, "description": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.", "rating": 6.7, "price": 1000, "poster": "https://i.pinimg.com/564x/d0/d2/a5/d0d2a5365c6de34873d5ae340574a6f6.jpg", "video_url": "https://youtu.be/QwievZ1Tx-8?si=bBX8tXlQbI1vWwFs", "genre": "Action"}
        ]

        for movie_data in movies_data:
            movie = Movies(title=movie_data['title'], year=movie_data['year'], description=movie_data['description'], rating=movie_data['rating'], price=movie_data['price'], poster=movie_data['poster'], trailer_url=movie_data['video_url'], genre=movie_data['genre'])
            db.session.add(movie)

        db.session.commit()
        print("Movies seeded successfully")

        print("Ontheatre_movies")

        ontheatre_data =[
            {""}
        ]

        


        print("Ontheatre_movies seeded successfully")







































        if __name__ == "__main__":
          seed_data()


