'''
Unit test code for Views
'''
from django.test import TestCase
from django.test.client import RequestFactory
from . views import twitter_user_id, tweet_view, create_tweet_form_view
import os
import twitter
from dotenv import load_dotenv

load_dotenv()

class SimpleTest(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.twitter_user_id = os.getenv('TWITTER_ID')
        self.api = twitter.Api(consumer_key=os.getenv('CUST_KEY'),
                  consumer_secret=os.getenv('CUST_SEC'),
                  access_token_key=os.getenv('OAUTH_TOKEN'),
                  access_token_secret=os.getenv('OAUTH_SEC'))


    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('tweets/show_tweet.html')

        response = create_tweet_form_view(request)
        self.assertEqual(response.status_code, 200)
