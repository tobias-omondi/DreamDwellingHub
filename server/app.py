from flask import Flask,make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api
from flask_migrate import Migrate
from flask_login import LoginManager, login_user,current_user
from models import db, User
from werkzeug.security import check_password_hash,generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

api = Api(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Home(Resource):
    def get(self):
        response_dict = {
            "message": "Welcome to RealEstate "
        }
        response = make_response(
            jsonify(response_dict),
            200,
        )
        return response
api.add_resource(Home, "/")


class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Missing email or password'}), 400

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.Password, password):
            login_user(user)
            return jsonify({'message': 'Logged in successfully'}), 200
        else:
            return jsonify({'message': 'Invalid email or password'}), 401
        
api.add_resource(Login, '/login')


class Signup(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'message': 'Missing email or password'}), 400

        if User.query.filter_by(email=email).first() is not None:
            return jsonify({'message': 'Email already exists'}), 400

        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(email=email, Password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User created successfully'}), 201

api.add_resource(Signup, '/signup')

if __name__ == '__main__':
    app.run(port=5550, debug=True)
