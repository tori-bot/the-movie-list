from flask import render_template
from . import main #import the blueprint instance main and use it to define our decorator

@main.app_errorhandler(404) #to use application-wide error handler we must use the app_errorhandler() decorator
def four_ow_four(error):
    #renders 404 error page
    return render_template('fourOwfour.html'),404