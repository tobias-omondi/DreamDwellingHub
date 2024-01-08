from app import app,db
from models import User,Notifications,RatingsReviews,Transaction,Company,Properties,PropertiesImages,News,Agent,Admin
from datetime import datetime

with app.app_context():

# seeding Users
   user1 = User(first_name = 'Alex', last_name = 'Wilison', email = 'alxeee@gmail.com',location = 'Nakuru',budgetrange = '$2,000,000')
   user1._password_hash='hashed_password'
   db.session.add(user1)
   db.session.commit()

   user2 = User(first_name = 'Tobias', last_name = 'Ogolla', email = 'tobiasogola42@gmail.com',location = 'Kisumu',budgetrange = '$6,000,000')
   user2._password_hash='hashed_password'
   db.session.add(user2)
   db.session.commit()

   user3 = User(first_name = 'Dan', last_name = 'Ndwinga', email = 'ndwinga@gmail.com',location = 'Athi River',budgetrange = '$5,000,000')
   user3._password_hash='hashed_password'
   db.session.add(user3)
   db.session.commit()

   user4 = User(first_name = 'Mercy', last_name = 'Wanjiru', email = 'mercywan20@gmail.com',location = 'Meru',budgetrange = '$4,500,000')
   user4._password_hash='hashed_password'
   db.session.add(user4)
   db.session.commit()


   user5 = User(first_name = 'Belza', last_name = 'Akinyi', email = 'belzaaa@gmail.com',location = 'Nairobi',budgetrange = '$7,800,000')
   user5._password_hash='hashed_password'
   db.session.add(user5)
   db.session.commit()

   user6 = User(first_name = 'Morgan', last_name = 'Mutwa', email = 'morganmtwa21@gmail.com',location = 'Machakos',budgetrange = '$10,000,000')
   user6._password_hash='hashed_password'
   db.session.add(user6)
   db.session.commit()