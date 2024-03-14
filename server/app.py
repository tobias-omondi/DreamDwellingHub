from flask import Flask,make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api
from flask_migrate import Migrate
from flask_login import LoginManager, login_user,current_user
from models import db, User,Properties,Transaction,Agent,Admin
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


class PropertyList(Resource):
    def get(self):
        properties = Properties.query.all()
        return {'properties': [property.name for property in properties]}

    def post(self):
        # Assuming you have a way to get the current user's ID
        user_id = current_user.id
        data = request.get_json()
        new_property = Properties(name=data['name'], bedrooms=data['bedrooms'], price=data['price'], amenities=data['amenities'], status=data['status'], location=data['location'], companies_id=user_id)
        db.session.add(new_property)
        db.session.commit()
        return {'message': 'Property created successfully'}, 201

api.add_resource(PropertyList, '/properties')


class TransactionList(Resource):
    def get(self):
        transactions = Transaction.query.all()
        return {'transactions': [transaction.transactiontype for transaction in transactions]}

    def post(self):
        data = request.get_json()
        new_transaction = Transaction(transactiontype=data['transactiontype'], amount=data['amount'], paymentstatus=data['paymentstatus'])
        db.session.add(new_transaction)
        db.session.commit()
        return {'message': 'Transaction created successfully'}, 201

api.add_resource(TransactionList, '/transactions')


class AgentList(Resource):
    def get(self):
        agents = Agent.query.all()
        return {'agents': [agent.name for agent in agents]}

    def post(self):
        data = request.get_json()
        new_agent = Agent(name=data['name'], email=data['email'], Phonenumber=data['Phonenumber'])
        db.session.add(new_agent)
        db.session.commit()
        return {'message': 'Agent created successfully'}, 201

api.add_resource(AgentList, '/agents')

class AdminList(Resource):
    def get(self):
        admins = Admin.query.all()
        return {'admins': [admin.fullname for admin in admins]}

    def post(self):
        data = request.get_json()
        new_admin = Admin(fullname=data['fullname'], email=data['email'], price=data['price'], Password=data['Password'], role=data['role'])
        db.session.add(new_admin)
        db.session.commit()
        return {'message': 'Admin created successfully'}, 201

api.add_resource(AdminList, '/admins')

from models import db, Notifications

class NotificationList(Resource):
    def get(self):
        notifications = Notifications.query.all()
        return {'notifications': [notification.message for notification in notifications]}

    def post(self):
        data = request.get_json()
        new_notification = Notifications(notificationsType=data['notificationsType'], message=data['message'], status=data['status'])
        db.session.add(new_notification)
        db.session.commit()
        return {'message': 'Notification created successfully'}, 201

api.add_resource(NotificationList, '/notifications')



if __name__ == '__main__':
    app.run(port=5550, debug=True)
