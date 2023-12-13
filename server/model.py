from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'users'
    id = db.Column (db.Integer, primary_key=True)
    first_name = db.Column (db.string, nullable = False)
    last_name = db.Column (db.String, nullable = False)
    email = db.Column (db.String, nullable = False)
    PreferedLocation = db.Column (db.String, nullable=False)
    budgetrange = db.Column ( db.String,nullable = False)
    Password = db.Column (db.String, nullable = False)
    

class Notifications (db.Model):
    __tablename__ = 'notifications'
    id = db.Column (db.Integer,primary_key = True)
    notificationsType = db.String (db.String, nullable = False)
    message = db.Column (db.String, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column (db.Column, nullable = False)

class RatingsReviews (db.Model):
    __tablename__ = 'ratingsreviews'
    id = db.Column (db.Integer, primary_key = True)
    ratings = db.Column (db.String, nullable = False)
    reviews = db.Column (db.String, nullable = False)
    reviewstest = db.Column (db.String, nullable = False)
    reviewsdate = db.Column (db.DateTime, default = datetime.utcnow)

class Transaction (db.Model):
    __tablename__ = 'transaction'
    id = db.Column (db.Integer, primary_key = True)
    transactiontype = db.Column (db.String, nullable = False)
    transactiondate = db.Column (db.DateTime, default = datetime.utcnow)
    amount = db.Column (db.Float, nullable = False)
    paymentstatus = db.Column (db.String, nullable = False)
    

class Company (db.Model):
    __tablename__ = 'companies'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.string, nullable = False)
    contactperson = db.Column (db.String, nullable = False)
    email = db.Column (db.String, nullable = False)
    Phonenumber = db.Column (db.String, nullable=False)
    location = db.Column ( db.String,nullable = False)
   


class Properties (db.Model):
    __tablename__ = 'properties'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.string, nullable = False)
    bedrooms= db.Column (db.String, nullable = False)
    price = db.Column (db.Float, nullable = False)
    amenities = db.Column (db.String, nullable=False)
    status = db.Column ( db.String,nullable = False)
    location = db.Column ( db.String,nullable = False)


class PropertiesImages (db.Model):
    __tablename__ = 'propertiesImages'
    id = db.Column (db.Integer, primary_key=True)
    img_url = db.Column (db.string, nullable = False)

class News (db.Model):
    __tablename__ = 'news'
    id = db.Column (db.Integer, primary_key=True)
    headlines = db.Column (db.string, nullable = False)
    news_img= db.Column (db.String, nullable = False)
    newspublication= db.Column (db.Float, nullable = False)
   
class Agent (db.Model):
    __tablename__ = 'agents'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.string, nullable = False)
    email= db.Column (db.String, nullable = False)
    Phonenumber= db.Column (db.Float, nullable = False)
    
class Admin (db.Model):
    __tablename__ = 'admin'
    id = db.Column (db.Integer, primary_key=True)
    fullname = db.Column (db.string, nullable = False)
    email= db.Column (db.String, nullable = False)
    price = db.Column (db.Float, nullable = False)
    Password = db.Column (db.String, nullable=False)
    role = db.Column ( db.String,nullable = False)
    

