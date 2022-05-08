from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE

simple=SimpleMDE()
mail=Mail()

login_manager=LoginManager()
login_manager.session_protection='strong'
#provides security level 'strong'
login_manager.login_view='auth.login'
#prefix the login endpoint with blueprint name because it is located inside the blueprint

photos=UploadSet('photos',IMAGES)

#create bootstrap instance
bootstrap=Bootstrap()
db = SQLAlchemy() #add psql database

def create_app(config_name):
    app=Flask(__name__) #create flask app instance

    #from_object() method imports config settings directly to application
    app.config.from_object(config_options[config_name])

    #configure UploadSet
    configure_uploads(app,photos)
    
    #call the init app method on an extension to complete initialization
    bootstrap.init_app(app)
    db.init_app(app) #create db instance
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    #register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    #setting auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    

    
    

    #will add the views and forms

    return app