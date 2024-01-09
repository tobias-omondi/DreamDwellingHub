from app import app,db
from models import User,Notifications,RatingsReviews,Transaction,Company,Properties,PropertiesImages,News,Agent,Admin
from datetime import datetime

with app.app_context():
   
# seeding Users
   user1 = User(first_name = 'Alex', last_name = 'Wilison', email = 'alxeee@gmail.com',location = 'Nakuru',budgetrange = '$2,000,000', Password = 'hashed_password')
   db.session.add(user1)
   db.session.commit()

   user2 = User(first_name = 'Tobias', last_name = 'Ogolla', email = 'tobiasogola42@gmail.com',location = 'Kisumu',budgetrange = '$6,000,000', Password = 'hashed_password')
   db.session.add(user2)
   db.session.commit()

   user3 = User(first_name = 'Dan', last_name = 'Ndwinga', email = 'ndwinga@gmail.com',location = 'Athi River',budgetrange = '$5,000,000', Password = 'hashed_password')
   db.session.add(user3)
   db.session.commit()

   user4 = User(first_name = 'Mercy', last_name = 'Wanjiru', email = 'mercywan20@gmail.com',location = 'Meru',budgetrange = '$4,500,000', Password = 'hashed_password')
   db.session.add(user4)
   db.session.commit()

   user5 = User(first_name = 'Belza', last_name = 'Akinyi', email = 'belzaaa@gmail.com',location = 'Nairobi',budgetrange = '$7,800,000', Password = 'hashed_password')
   db.session.add(user5)
   db.session.commit()

   user6 = User(first_name = 'Morgan', last_name = 'Mutwa', email = 'morganmtwa21@gmail.com',location = 'Machakos',budgetrange = '$10,000,000', Password = 'hashed_password')
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

# seeding RatingsReviews
   RatingsReview1 = RatingsReviews(ratings='5', reviews='Great place!', reviewstest='Test review', reviewsdate=datetime(2024, 1, 1, 8, 0, 0), user_id=1, company_id=1, property_id=1)
   db.session.add(RatingsReview1)
   db.session.commit()

   RatingsReview2 = RatingsReviews(ratings='4', reviews='Good service!', reviewstest='Positive ', reviewsdate=datetime(2024, 8, 5, 10, 0, 0), user_id=2, company_id=2, property_id=2)
   db.session.add(RatingsReview2)
   db.session.commit()

   RatingsReview3 = RatingsReviews(ratings='3.8', reviews='Needs improvement !', reviewstest='Negative', reviewsdate=datetime(2023, 7, 1, 10, 0, 0), user_id=2, company_id=2, property_id=3)
   db.session.add(RatingsReview3)
   db.session.commit()

   RatingsReview4 = RatingsReviews(ratings='4.5', reviews='Good service!', reviewstest='Positive ', reviewsdate=datetime(2024, 4, 1, 10, 0, 0), user_id=2, company_id=2, property_id=4)
   db.session.add(RatingsReview4)
   db.session.commit()

   RatingsReview5 = RatingsReviews(ratings='5', reviews=' Highly recommended  !', reviewstest='Another test review', reviewsdate=datetime(2023, 8, 1, 10, 0, 0), user_id=2, company_id=2, property_id=5)
   db.session.add(RatingsReview5)
   db.session.commit()

   RatingsReview6 = RatingsReviews(ratings='5', reviews='  Satisfied with the service!', reviewstest='Another test review', reviewsdate=datetime(2023, 4, 1, 10, 0, 0), user_id=2, company_id=2, property_id=6)
   db.session.add(RatingsReview6)
   db.session.commit()

# seeding Transactions
   Transaction1 = Transaction(transactiontype='Buy', transactiondate=datetime(2024, 1, 1, 8, 0, 0), amount=2000000.00, paymentstatus='Paid', user_id=1, property_id=1)
   db.session.add(Transaction1)
   db.session.commit()

   Transaction2 = Transaction(transactiontype='Rent', transactiondate=datetime(2024, 2, 1, 8, 0, 0), amount=1000000.00, paymentstatus='Pending', user_id=2, property_id=2)
   db.session.add(Transaction2)
   db.session.commit()

   Transaction3 = Transaction(transactiontype='Lease', transactiondate=datetime(2024, 3, 1, 8, 0, 0), amount=1500000.00, paymentstatus='Paid', user_id=3, property_id=3)
   db.session.add(Transaction3)
   db.session.commit()

   Transaction4 = Transaction(transactiontype='Buy', transactiondate=datetime(2024, 4, 1, 8, 0, 0), amount=2500000.00, paymentstatus='Pending', user_id=4, property_id=4)
   db.session.add(Transaction4)
   db.session.commit()

   Transaction5 = Transaction(transactiontype='Rent', transactiondate=datetime(2024, 5, 1, 8, 0, 0), amount=1200000.00, paymentstatus='Paid', user_id=5, property_id=5)
   db.session.add(Transaction5)
   db.session.commit()

   Transaction6 = Transaction(transactiontype='Lease', transactiondate=datetime(2024, 6, 1, 8, 0, 0), amount=1800000.00, paymentstatus='Pending', user_id=6, property_id=6)
   db.session.add(Transaction6)
   db.session.commit()

# Seeding Companies
   Company1 = Company(name='Real Estate', contactperson='Alex k', email='alexk@gmail.com', Phonenumber='+254741041580', location='Nakuru')
   db.session.add(Company1)
   db.session.commit()

   Company1 = Company(name='XYZ Properties ', contactperson='Henry winny', email='henrywil@gmail.com', Phonenumber='+25474158941580', location='Kisumu')
   db.session.add(Company1)
   db.session.commit()

   Company1 = Company(name='Dream Homes Inc.', contactperson='Harry Potter', email='potter1@gmail.com', Phonenumber='+254751041580', location='Athi River')
   db.session.add(Company1)
   db.session.commit()


   Company1 = Company(name=' Elite Estates ', contactperson='James mILNER', email='milner23@gmail.com', Phonenumber='+254762041580', location='Nairobi')
   db.session.add(Company1)
   db.session.commit()

   Company1 = Company(name=' Prime Properties', contactperson='Frank', email='frank1@gmail.com', Phonenumber='+254741023480', location='Meru')
   db.session.add(Company1)
   db.session.commit()


   Company1 = Company(name='KingStone town', contactperson='Abdifatar', email='abdifatar@gmail.com', Phonenumber='+254741041345', location='Kisumu')
   db.session.add(Company1)
   db.session.commit()

   Company1 = Company(name='Real Estate', contactperson='Alex k', email='email1@example.com', Phonenumber='+254741041580', location='Nakuru')
   db.session.add(Company1)
   db.session.commit()

# seeding properties

   Property1 = Properties(name='Spacious Family Home', bedrooms='4', price=500000.00, amenities='Garden, Pool, Garage', status='Available', location='Nairobi', company_id=1)
   db.session.add(Property1)
   db.session.commit()

   Property2 = Properties(name='Modern City Apartment', bedrooms='6', price=300000.00, amenities='Gym, Balcony, City View', status='Sold', location='Kisumu', company_id=2)
   db.session.add(Property2)
   db.session.commit()

   Property3 = Properties(name='Cozy Suburban Townhouse', bedrooms='4', price=400000.00, amenities='Fireplace, Patio, Parking', status='Available', location='Nairobi', company_id=1)
   db.session.add(Property3)
   db.session.commit()

   Property4 = Properties(name='Luxury Beachfront Villa', bedrooms='5', price=1200000.00, amenities='Private Beach Access, Pool', status='Available', location='Mombasa', company_id=3)
   db.session.add(Property4)
   db.session.commit()

   Property5 = Properties(name='Downtown Penthouse', bedrooms='5', price=800000.00, amenities='Rooftop Terrace, Skyline View', status='Sold', location='Siaya', company_id=4)
   db.session.add(Property5)
   db.session.commit()

   Property5 = Properties(name='Penthouse', bedrooms='7', price=1200000.00, amenities='Rooftop Terrace, Skyline View', status='Sold', location='Meru', company_id=5)
   db.session.add(Property5)
   db.session.commit()
 
   Property5 = Properties(name='Beachfront Villa', bedrooms='5', price=900000.00, amenities='Private Beach Access, Pool', status='Available', location='Mombasa', company_id=6)
   db.session.add(Property5)
   db.session.commit()

# propertiesImages

   PropertyImage1 = PropertiesImages(img_url='https://www.wondersofwatamu.com/cache/ce_img_cache/local/44ae9cb623a198e2/watamu_property_2_770_520_70_s.jpg')
   PropertyImage1.properties = Property1
   db.session.add(PropertyImage1)
   db.session.commit()

   PropertyImage2 = PropertiesImages(img_url='https://bosworthpropertymarrakech.com/wp-content/uploads/2023/03/bosworthpropertymarrakech-54-1-750x500.jpg')
   PropertyImage2.properties = Property2
   db.session.add(PropertyImage2)
   db.session.commit()

   PropertyImage3 = PropertiesImages(img_url='https://housing.com/news/wp-content/uploads/2023/01/modern-villa-designs-FEATURE-compressed.jpg')
   PropertyImage3.properties = Property3
   db.session.add(PropertyImage3)
   db.session.commit()

   PropertyImage4 = PropertiesImages(img_url='https://images.pamgolding.co.za/content/properties/202312/2096286/h/2096286_h_2.jpg?w=600&quality=75')
   PropertyImage4.properties = Property4
   db.session.add(PropertyImage4)
   db.session.commit()

   PropertyImage5 = PropertiesImages(img_url='https://properties.fairdeal.co.ke/images/thumbnail/6.jpg')
   PropertyImage5.properties = Property5
   db.session.add(PropertyImage5)
   db.session.commit()

# seeding News
   News1 = News(headlines='Exciting Real Estate Trends  ', news_img='image_url_1', newspublication='January 5, 2024  ', company_id = 1)
   db.session.add(News1)
   db.session.commit()

   News2 = News(headlines='Market Update: Q2 2023   ', news_img='image_url_2', newspublication='June 15, 2023 ', company_id = 2)
   db.session.add(News2)
   db.session.commit()

   News3 = News(headlines='Award-Winning Architecture  ', news_img='image_url_2', newspublication='October 12, 2023 ' ,company_id = 3)
   db.session.add(News3)
   db.session.commit()

   News4 = News(headlines='Sustainable Living   ', news_img='image_url_2', newspublication='February 28, 2024 ', company_id = 4)
   db.session.add(News4)
   db.session.commit()

   News5 = News(headlines='Innovations in Urban Planning ', news_img='image_url_2', newspublication='April 3, 2024 ', company_id =5)
   db.session.add(News5)
   db.session.commit()

# seeding Agents
   Agent1 = Agent(name='Peter sila', email='petersila@gmail.com', Phonenumber='1234567890', company_id =1)
   db.session.add(Agent1)
   db.session.commit()

   Agent2 = Agent(name='James Madision', email='jamesmadison@gmail.com', Phonenumber='0987654321', company_id = 2)
   db.session.add(Agent2)
   db.session.commit()

   Agent3 = Agent(name='Pochetinyo', email='pochetinyo@gmail.com.com', Phonenumber='9407654321', company_id = 3)
   db.session.add(Agent3)
   db.session.commit()

   Agent4 = Agent(name='Wizardb', email='wizardb@gmail.com', Phonenumber='39305054321', company_id = 4)
   db.session.add(Agent4)
   db.session.commit()

   Agent5 = Agent(name='Martin wig', email='martinwig@gmail.com.com', Phonenumber='1123454321', company_id = 5)
   db.session.add(Agent5)
   db.session.commit()

   Agent6 = Agent(name='Thomas', email='thomas@gmail.com', Phonenumber='0767654321', company_id = 6)
   db.session.add(Agent6)
   db.session.commit()

# seeding Admins
   Admin1 = Admin(fullname='Tobias Ogola', email='tobiasogola@gmail.com', price=100.00, Password='hashed_password', role='Admin')
   db.session.add(Admin1)
   db.session.commit()

   Admin2 = Admin(fullname='Mary Agatha', email='maryagathagmail.com', price=200.00, Password='hashed_password', role='admin')
   db.session.add(Admin2)
   db.session.commit()





