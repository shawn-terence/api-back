from app import app
from models import User, Movies, Ontheatre, db

def seed_data():
    # Delete existing data from tables
    db.session.query(User).delete()
    db.session.query(Movies).delete()
    db.session.query(Ontheatre).delete()

    # Create sample users
    user1 = User(username='john_doe', gmail='john@example.com')
    user1.set_password('password123')
    
    user2 = User(username='jane_doe', gmail='jane@example.com')
    user2.set_password('password456')
    
    # Add sample users to the session
    db.session.add(user1)
    db.session.add(user2)
    
    # Commit users to the database
    db.session.commit()

    # Create sample movies
    movie1 = Movies(title='Movie1', year=2021, description='Description for Movie1', rating=7.5, price=10,
                    poster='poster1.jpg', trailer_url='trailer1_url', genre='Action')
    
    movie2 = Movies(title='Movie2', year=2022, description='Description for Movie2', rating=8.0, price=12,
                    poster='poster2.jpg', trailer_url='trailer2_url', genre='Comedy')
    
    # Add sample movies to the session
    db.session.add(movie1)
    db.session.add(movie2)
    
    # Commit movies to the database
    db.session.commit()

    # Create sample Ontheatre
    ontheatre1 = Ontheatre(movie_id=movie1.id, runtime=120, seats='A1,A2,A3', title='Movie1', year=2021,
                           description='Description for Ontheatre1', rating_theater=7.5, price_theater=15,
                           poster_theater='poster1_theater.jpg', trailer_url_theater='trailer1_url_theater',
                           genre_theater='Action')
    
    ontheatre2 = Ontheatre(movie_id=movie2.id, runtime=110, seats='B1,B2,B3', title='Movie2', year=2022,
                           description='Description for Ontheatre2', rating_theater=8.0, price_theater=18,
                           poster_theater='poster2_theater.jpg', trailer_url_theater='trailer2_url_theater',
                           genre_theater='Comedy')
    
    # Add sample Ontheatre to the session
    db.session.add(ontheatre1)
    db.session.add(ontheatre2)
    
    # Commit Ontheatre to the database
    db.session.commit()
    
    print('Seed data has been added to the database.')

if __name__ == '__main__':
    with app.app_context():
        # Seed the database with initial data
        seed_data()
