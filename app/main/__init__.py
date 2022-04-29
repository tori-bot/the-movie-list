from ensurepip import bootstrap
from flask import Blueprint
main=Blueprint('main',__name__)
# initialize the Blueprint class by creating a variable main. The Blueprint class takes in 2 arguments. The name of the blueprint and the __name__ variable to find the location of the blueprint

from . import views,errors
#to avoid circular dependencies

#register a blueprint
def create_app(config_name):
    app=Flask(__name__)

    #create app configs
    app.config.from_object(config_options[config_name] )

    #initialize flask extensions
    bootstrap.init_app(app)

    #register the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app