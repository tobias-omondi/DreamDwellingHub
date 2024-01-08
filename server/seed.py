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

# seeding Notifications
Notifications1 = Notifications(notificationsType='Reminder', message='New properties available', created_at=datetime.strptime('2024-01-01 08:00:00', '%Y-%m-%d %H:%M:%S'), status='unread', user_id=1)
db.session.add(Notifications1)
db.session.commit()

Notifications2 = Notifications(notificationsType='Alert', message='Check out our latest news!', created_at=datetime.strptime('2024-01-01 08:00:00', '%Y-%m-%d %H:%M:%S'), status='read', user_id=2)
db.session.add(Notifications2)
db.session.commit()

Notifications3 = Notifications(notificationsType='Alert', message='This might get your attention', created_at=datetime.strptime('2023-08-01 10:00:00', '%Y-%m-%d %H:%M:%S'), status='unread', user_id=3)
db.session.add(Notifications3)
db.session.commit()

Notifications4 = Notifications(notificationsType='Information', message='Your appointment is Tomorrow', created_at=datetime.strptime('2024-01-02 08:00:00', '%Y-%m-%d %H:%M:%S'), status='read', user_id=4)
db.session.add(Notifications4)
db.session.commit()

Notifications5 = Notifications(notificationsType='Request', message='Check out our latest news!', created_at=datetime.strptime('2024-01-01 08:00:00', '%Y-%m-%d %H:%M:%S'), status='read', user_id=5)
db.session.add(Notifications5)
db.session.commit()

Notifications6 = Notifications(notificationsType='Information', message='Your message is being Reviewed', created_at=datetime.strptime('2023-10-01 11:00:00', '%Y-%m-%d %H:%M:%S'), status='unread', user_id=6)
db.session.add(Notifications6)
db.session.commit()