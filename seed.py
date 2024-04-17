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
            {"title": "Avengers: Infinity War", "year": 2018, "description": "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.", "rating": 6.7, "price": 1000, "poster": "https://i.pinimg.com/564x/d0/d2/a5/d0d2a5365c6de34873d5ae340574a6f6.jpg", "video_url": "https://youtu.be/QwievZ1Tx-8?si=bBX8tXlQbI1vWwFs", "genre": "Action"},
            {"title": "Dune 2", "year": 2024, "description": " Dune 2 is a captivating science fiction epic set in a distant future where noble houses control various planets across the universe.", "rating": 8.9, "price": 850, "poster": "https://lh3.googleusercontent.com/proxy/aYvh5RafjQmFiHjOwRcN3kRO60c4s61UtZR87Ab6-j_w76Lm_mZE3i_sAvhJkyx7s43xvxO3amNS-J1jjaIX8pwxEAqeZvmaa0TfVeu-cg", "video_url": "https://youtu.be/U2Qp5pL3ovA?si=Q9tdt31ntDkgH_8H", "genre": "Science fiction"},
            {"title": "Transformers Rise Of The Beast", "year": 2022, "description": "Transformers Rise of the Beasts is an electrifying addition to the iconic Transformers franchise. Set in a world where humans coexist with powerful alien robots, the film takes audiences on a thrilling journey through time and space. .", "rating": 9.5, "price": 900, "poster": "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p20201199_v_h10_am.jpg", "video_url": "https://youtu.be/itnqEauWQZM?si=GVglv_XpGr7Ncnqy", "genre": "Action"}
        ]

        for movie_data in movies_data:
            movie = Movies(title=movie_data['title'], year=movie_data['year'], description=movie_data['description'], rating=movie_data['rating'], price=movie_data['price'], poster=movie_data['poster'], trailer_url=movie_data['video_url'], genre=movie_data['genre'])
            db.session.add(movie)

        db.session.commit()
        print("Movies seeded successfully")

    print("Seeding users")

    users_data = [
        {"username": "user1", "gmail": "user1@gmail.com", "password": "password1"},
        {"username": "user2", "gmail": "user2@gmail.com", "password": "password2"},
        {"username": "user3", "gmail": "user3@gmail.com", "password": "password3"},
        {"username": "user4", "gmail": "user4@gmail.com", "password": "password4"},
        {"username": "user5", "gmail": "user5@gmail.com", "password": "password5"}
    ]

    for user_data in users_data:
        user = User(username=user_data['username'], gmail=user_data['gmail'], password=user_data['password'])
        db.session.add(user)

    db.session.commit()
    print("Users seeded successfully")

    print("Seeding Theater Data")

    theater_data = [
        {
            "movie_id": 1,
            "runtime": 120,
            "seats": "A1,A2,A3,B1,B2,B3,C1,C2,C3",
            "title": "The Amazing Spider-Man",
            "year": 2014,
            "description": "After Peter Parker is bitten by a genetically altered spider, he gains newfound, spider-like powers and ventures out to save the city from the machinations of a mysterious reptilian foe.",
            "rating_theater": 7.5,
            "poster_theater": "https://i.pinimg.com/564x/c5/7e/b6/c57eb61ecc25097a4a3682238efe3d5d.jpg",
            "trailer_url_theater": "https://youtu.be/-tnxzJ0SSOw?si=5KIJncsQKKggyzxM",
            "genre_theater": "Action",
            "price_theater": 700
        },
        {
            "movie_id": 2,
            "runtime": 130,
            "seats": "A1,A2,A3,B1,B2,B3,C1,C2,C3",
            "title": "Fast and Furious 6",
            "year": 2013,
            "description": "Hobbs has Dominic and Brian reassemble their crew to take down a team of mercenaries: Dominic unexpectedly gets sidetracked with facing his presumed deceased girlfriend, Letty.",
            "rating_theater": 6.7,
            "poster_theater": "https://i.pinimg.com/564x/19/2a/66/192a66022855d80ea8f95c930382f914.jpg",
            "trailer_url_theater": "https://youtu.be/oc_P11PNvRs?si=ObjTbpV4KFohk7NP",
            "genre_theater": "Action",
            "price_theater": 500
        },
        {
            "movie_id": 3,
            "runtime": 130,
            "seats": "A1,A2,A3,B1,B2,B3,C1,C2,C3",
            "title": "Avengers: Infinity War",
            "year": 2013,
            "description": ".",
            "rating_theater": 6.7,
            "poster_theater": "https://i.pinimg.com/564x/19/2a/66/192a66022855d80ea8f95c930382f914.jpg",
            "trailer_url_theater": "https://youtu.be/oc_P11PNvRs?si=ObjTbpV4KFohk7NP",
            "genre_theater": "Action",
            "price_theater": 500
        },
        {
            "movie_id": 4,
            "runtime": 130,
            "seats": "A1,A2,A3,B1,B2,B3,C1,C2,C3",
            "title": "Dune2",
            "year": 2013,
            "description": "Dune is a captivating science fiction epic set in a distant future where noble houses control various planets across the universe.",
            "rating_theater": 8.9,
            "poster_theater": "https://lh3.googleusercontent.com/proxy/aYvh5RafjQmFiHjOwRcN3kRO60c4s61UtZR87Ab6-j_w76Lm_mZE3i_sAvhJkyx7s43xvxO3amNS-J1jjaIX8pwxEAqeZvmaa0TfVeu-cg",
            "trailer_url_theater": "https://youtu.be/U2Qp5pL3ovA?si=Q9tdt31ntDkgH_8H",
            "genre_theater": "Science fiction",
            "price_theater": 850
        },
        {
            "movie_id": 5,
            "runtime": 130,
            "seats": "A1,A2,A3,B1,B2,B3,C1,C2,C3",
            "title": "Transformers Rise Of The Beast",
            "year": 2022,
            "description": "Transformers: Rise of the Beasts is an electrifying addition to the iconic Transformers franchise. Set in a world where humans coexist with powerful alien robots, the film takes audiences on a thrilling journey through time and space.",
            "rating_theater": 9.5,
            "poster_theater": "https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p20201199_v_h10_am.jpg",
            "trailer_url_theater": "https://youtu.be/itnqEauWQZM?si=GVglv_XpGr7Ncnqy",
            "genre_theater": "Action",
            "price_theater": 900
        },
    ]

    for data in theater_data:
        theater = Ontheatre(
            movie_id=data['movie_id'],
            runtime=data['runtime'],
            seats=data['seats'],
            title=data['title'],
            year=data['year'],
            description=data['description'],
            rating_theater=data['rating_theater'],
            poster_theater=data['poster_theater'],
            trailer_url_theater=data['trailer_url_theater'],
            genre_theater=data['genre_theater'],
            price_theater=data['price_theater']
        )
        db.session.add(theater)

    db.session.commit()
    print("Theater data seeded successfully")

# Call the seed_data function to seed the data
seed_data()
