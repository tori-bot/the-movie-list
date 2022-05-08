from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    #function queries db and gets user with an id
    return User.query.get(int(user_id))

class Role(db.Model):
    #create a role that will define all different roles
    __tablename__='roles'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))
    users=db.relationship('User',backref='role',lazy="dynamic")
    
    #db.relationship creates a virtual column to connct with foreign key(class,backref,lazy)

    #backref allows access and sets our class eg to get the role of user we run user.role
    
    #lazy is how sqlalcemy loads our project. In this case our objects will be loaded and filtered before returning

    def __repr__(self):
        return f'User {self.name} '


class User(UserMixin,db.Model):
    #class to create new users. connect user class to our db aand allow communication
    __tablename__='users'

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255),index=True)
    email=db.Column(db.String(255),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio=db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    password_secure=db.Column(db.String(255))
    reviews=db.relationship('Review',backref='user',lazy="dynamic" )
    # pass_secure=db.Column(db.String(255))
    # password_hash=db.Column(db.String(255))


    @property
    def password(self):
        #create a write only class property (password)
        raise AttributeError('you cannot read the password attribute')
        #to block access of user to the password property

    @password.setter
    def password(self,password):
        #generate pssword hash
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        #compare a password to the hashed password to check of they are same
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username} '

class Review(db.Model):
    __tablename__='reviews'

    id=db.Column(db.Integer,primary_key=True)
    movie_id=db.Column(db.Integer)
    movie_title=db.Column(db.String)
    movie_path=db.Column(db.String)
    movie_review=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,index):
        reviews=Review.query.filter_by(movie_id=index).all()
        return reviews

class Movie:
    #class to define movie objects
    def __init__(self,index,title,overview,poster,vote_average,vote_count):
        self.index=index
        self.title=title
        self.overview=overview
        self.poster='https://image.tmdb.org/t/p/w500/'+poster
        self.vote_average=vote_average
        self.vote_count=vote_count


# class Reviews:
#     all_reviews=[]

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id=movie_id
#         self.title=title
#         self.imageurl=imageurl
#         self.review=review

#     def save_review(self):
#         Reviews.all_reviews.append(self)

#     @classmethod
#     def get_reviews(cls,index):
#         response=[]

#         for review in cls.all_reviews:
#             if review.movie_id==index:
#                 response.append(review)

#         return response
         

#     @classmethod
#     def clear_reviews(cls):
#         Reviews.all_reviews.clear()
    
