from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User,Notifications,News,RatingsReviews,Company,Properties,PropertiesImages,Admin,Agent,Transaction


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate (app,db)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ =='__main__':
    app.run(port=5555)
