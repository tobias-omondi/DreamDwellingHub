from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy()

class User (db.Model):
    __tablename__ = 'users'
    id = db.Column (db.Integer, primary_key=True)
    first_name = db.Column (db.String, nullable = False)
    last_name = db.Column (db.String, nullable = False)
    email = db.Column (db.String, nullable = False)
    location = db.Column (db.String, nullable=False)
    budgetrange = db.Column ( db.String,nullable = False)
    Password = db.Column (db.String, nullable = False)

    # Relationship
    notificationsprocess = db.relationship ('Notifications', back_populates = 'users')
    ratingsreviews = db.relationship ('RatingsReviews', back_populates = 'users')
    transaction = db.relationship ('Transaction', back_populates = 'users')
    

class Notifications (db.Model):
    __tablename__ = 'notifications'
    id = db.Column (db.Integer,primary_key = True)
    notificationsType = db.Column (db.String, nullable = False)
    message = db.Column (db.String, nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column (db.Column, nullable = False)

    # Relationship
    user = db.relationship ('User' , back_populates = 'notifications')

class RatingsReviews (db.Model):
    __tablename__ = 'ratingsreviews'
    id = db.Column (db.Integer, primary_key = True)
    ratings = db.Column (db.String, nullable = False)
    reviews = db.Column (db.String, nullable = False)
    reviewstest = db.Column (db.String, nullable = False)
    reviewsdate = db.Column (db.DateTime, default = datetime.utcnow)

    # Relationship
    users = db.relationship ('User',back_populates = 'ratingsreviews' )
    company = db.relationship ('Company' , back_populates ='ratingsreviews')
    property = db.relationship ('Properties' , back_populates = 'ratingsreviews')

class Transaction (db.Model):
    __tablename__ = 'transactions'
    id = db.Column (db.Integer, primary_key = True)
    transactiontype = db.Column (db.String, nullable = False)
    transactiondate = db.Column (db.DateTime, default = datetime.utcnow)
    amount = db.Column (db.Float, nullable = False)
    paymentstatus = db.Column (db.String, nullable = False)

    # relationship
    user = db.relationship ('User', back_populates = 'transactions')
    property= db.relationship ('Properties', back_populates = 'transactions')
    

class Company (db.Model):
    __tablename__ = 'companies'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String, nullable = False)
    contactperson = db.Column (db.String, nullable = False)
    email = db.Column (db.String, nullable = False)
    Phonenumber = db.Column (db.String, nullable=False)
    location = db.Column ( db.String,nullable = False)

    # Relationship
    property = db.relationship ('Properties' , back_populates = 'companies')
    ratingsreviews1 = db.relationship ('RatingsReviews', back_populates = 'companies')
    news = db.relationship ('News', back_populates = 'companies')
    agent = db.relationship ('Agent', back_populates = 'companies')
   


class Properties (db.Model):
    __tablename__ = 'properties'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String, nullable = False)
    bedrooms= db.Column (db.String, nullable = False)
    price = db.Column (db.Float, nullable = False)
    amenities = db.Column (db.String, nullable=False)
    status = db.Column ( db.String, nullable = False)
    location = db.Column ( db.String,nullable = False)

    # Relationship
    company = db.relationship ('Company' , back_populates = 'properties')
    property = db.relationship ('Properties', back_populates = 'properties')
    transaction = db.relationship ('Transaction', back_populates = 'properties')
    properties_images = db.relationship ('PropertiesImages', back_populates = 'properties')


class PropertiesImages (db.Model):
    __tablename__ = 'propertiesImages'
    id = db.Column (db.Integer, primary_key=True)
    img_url = db.Column (db.String, nullable = False)

    # Relationship
    property = db.relationship ('Properties' , back_populates = 'propertiesImages')

class News (db.Model):
    __tablename__ = 'news'
    id = db.Column (db.Integer, primary_key=True)
    headlines = db.Column (db.string, nullable = False)
    news_img= db.Column (db.String, nullable = False)
    newspublication= db.Column (db.String, nullable = False)

    # relationship
    company = db.relationship ('Company' , back_populates = 'news')
   
class Agent (db.Model):
    __tablename__ = 'agents'
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.string, nullable = False)
    email= db.Column (db.String, nullable = False)
    Phonenumber= db.Column (db.String, nullable = False)

    # Relationship
    company= db.relationship ('Company' , back_populates = 'agents')
    
class Admin (db.Model):
    __tablename__ = 'admin'
    id = db.Column (db.Integer, primary_key=True)
    fullname = db.Column (db.string, nullable = False)
    email= db.Column (db.String, nullable = False)
    price = db.Column (db.Float, nullable = False)
    Password = db.Column (db.String, nullable=False)
    role = db.Column ( db.String,nullable = False)
    

