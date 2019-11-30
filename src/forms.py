'''
Form UI Class for the Twitter API Operations

Author: Kevin Lai
'''
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, Length

class CreateTweetForm(FlaskForm):
	description = TextAreaField('description', validators=[InputRequired(), Length(min = 1, max = 280)])
	create_confirm = SubmitField('Create Tweet')

class DeleteTweetForm(FlaskForm):
	tweet_id = IntegerField('tweet_id', validators=[InputRequired()])
	delete_confirm = SubmitField('Delete Tweet')