import os
#allow the app to interact with the os dependent functionality

class Config:#used in both prod & dev stages of app
    #general configuration parent class
    MOVIE_API_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    #{} section of url tat is replaced by actual values
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #set these 2 above as environment variables

class ProdConfig(Config):
    #production configuration child class
    pass

class DevConfig(Config):
    #development configuration child class
    DEBUG=True#enable debug mode in application

#dict to help us access different config option classes
config_options={
    'development':DevConfig,
    'production':ProdConfig
}