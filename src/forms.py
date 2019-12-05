'''
Form UI Class for the Twitter API Operations

Author: Kevin Lai
'''
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
#from wtforms import InputField
# InputField validator does not work with AutoComplete data
# Use InputField validator for secondary confirmation, like to confirm email

class CreateTweetForm(FlaskForm):
	description = TextAreaField('description', validators=[DataRequired(), Length(min = 1, max = 280)])
	create_confirm = SubmitField('Create Tweet')

class DeleteTweetForm(FlaskForm):
	tweet_id = IntegerField('tweet_id', validators=[DataRequired()])
	delete_confirm = SubmitField('Delete Tweet')
