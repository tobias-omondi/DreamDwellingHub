from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_migrate import Migrate
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User,Notifications,News,RatingsReviews,Company,Properties,PropertiesImages,Admin,Agent,Transaction
from form import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate (app,db)

db.init_app(app)

@app.route('/signup', methods = ['POST'])
def signup():
    form = RegistrationForm(request.form)
    if form.validate():
        user = user(
            first_name = form.first_name.data,
             last_name=form.last_name.data,
            email=form.email.data,
            location=form.location.data,
            budgetrange=form.budgetrange.data,
            Password=form.password.data 
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({'error': 'Validation failed', 'errors': form.errors}), 400
    
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=True) 
            return redirect(url_for('index')) 
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html') 

if __name__ =='__main__':
    app.run(port=5550,debug=True)
