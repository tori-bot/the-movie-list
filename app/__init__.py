from ensurepip import bootstrap
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap


#create bootstrap instance
bootstrap=Bootstrap()

def create_app(config_name):
    app=Flask(__name__) #create flask app instance

    #from_object() method imports config settings directly to application
    app.config.from_object(config_options[config_name])

    #call the init app method on an extension to complete initialization
    bootstrap.init_app(app)

    #register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from .requests import configure_request
    configure_request(app)

    #will add the views and forms

    return app