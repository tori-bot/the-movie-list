import os
from re import T
#allow the app to interact with the os dependent functionality


class Config:#used in both prod & dev stages of app
    #general configuration parent class
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    #{} section of url tat is replaced by actual values
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #set these 2 above as environment variables

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/watchlist'
    #add link to database

    #specify destination to save uploaded images
    UPLOAD_PHOTOS_DEST='app/static/photos'

    #email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("makenavictoria1@gmail.com")
    MAIL_PASSWORD="golden5626era.?!"

#simple mde configurations
    SIMPLEMDE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class ProdConfig(Config):
    #production configuration child class
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    

class DevConfig(Config):
    #development configuration child class
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/watchlist'
    
    DEBUG=True#enable debug mode in application

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/watchlist_test'

#dict to help us access different config option classes
config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}