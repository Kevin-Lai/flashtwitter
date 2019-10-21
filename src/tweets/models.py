'''
Models for tweet app

Author: Vignesh Kumar T
'''
from django.db import models

# Create your models here.
class CreateTweet(models.Model):
	description = models.TextField(blank=False, null=False)

class DeleteTweet(models.Model):
	tweet_id = models.IntegerField(blank=False, null=False)

class User(models.Model):
	user_id = models.TextField(blank=False, null=False)
