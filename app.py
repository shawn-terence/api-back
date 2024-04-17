from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity,create_access_token
from flask_migrate import Migrate
from models import db, User,Movies,Ontheatre
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flickfusion.db'
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)




def check_password(user, password):
    return check_password_hash(user.password, password)
    
def set_password(user, password):
    user.password = generate_password_hash(password)

def generate_token(user):
    access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(days=1))
    return access_token
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(username=data['username'], gmail=data['gmail'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and check_password(user, data['password']):
        token = generate_token(user)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if user:
        return jsonify({'message': f'Hello, {user.username}'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    
from flask import render_template

@app.route('/')
def index():
    return f"Welcome to Flick Fusion API"

    
@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movies.query.all()
    return jsonify([movie.serialize() for movie in movies])

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movies.query.get(movie_id)
    if movie:
        return jsonify(movie.serialize())
    else:
        return jsonify({"error": "Movie not found"}), 404
    
@app.route('/ontheatre', methods=['GET'])
def get_ontheatre():
    ontheatre = Ontheatre.query.all()
    return jsonify([ontheatre_item.serialize() for ontheatre_item in ontheatre])

@app.route('/ontheatre/<int:ontheatre_id>', methods=['GET'])
def get_ontheatre_by_id_endpoint(ontheatre_id):
    ontheatre = Ontheatre.query.get(ontheatre_id)
    if ontheatre:
        return jsonify(ontheatre.serialize())
    else:
        return jsonify({"error": "Ontheatre movies not found"}), 404







    



















if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
