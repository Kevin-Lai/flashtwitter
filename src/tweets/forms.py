from django import forms

from .models import CreateTweet, DeleteTweet, User

class CreateTweetForm(forms.ModelForm):
	class Meta:
		model = CreateTweet
		fields = [
			'description'
		]

class DeleteTweetForm(forms.ModelForm):
	class Meta:
		model = DeleteTweet
		fields = [
			'tweet_id'
		]

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'user_id'
		]
