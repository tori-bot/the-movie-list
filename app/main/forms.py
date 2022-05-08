from flask_wtf import FlaskForm #to create form class
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired # prevent the user from submitting the form without Inputting a value

class ReviewForm(FlaskForm): 
    #ReviewForm class inherits from FlaskForm class
    title=StringField('Review title',validators=[InputRequired()]) #(label,list of validators)
    review=TextAreaField('Movie review')
    submit=SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio=TextAreaField('Tell us about you.',validators=[InputRequired()])
    submit=SubmitField('Submit')