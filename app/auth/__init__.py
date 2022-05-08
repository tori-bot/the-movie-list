from flask import Blueprint

auth=Blueprint('auth',__name__)
#create a blueprint instance auth and import auth views module
from . import views,forms