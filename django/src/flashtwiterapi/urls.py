"""flashtwiterapi URL Configuration

Author: Team Flash

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# Added to link to views.py - Kevin Lai
# Each time you create a new page, you need to import it here.
from webpages.views import homepage_view, signin_view, signup_view, test_view
from tweets.views import tweet_view, create_tweet_form_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Regular Pages for the Web App - Kevin Lai
    path('', homepage_view, name="homepage"),
    path('home/', homepage_view, name="homepage"),
    path('signin/', signin_view, name="signin"),
    path('signup/', signup_view, name="signup"),

    # Forms for accessing Twitter API - Kevin Lai
    path('create_tweet/', create_tweet_form_view, name='create_tweet'),
    path('show_tweet/', tweet_view, name='show_tweet'),

    # For testing only. Be sure to comment out if not testing. - Kevin Lai
    path('test/', test_view, name="test"),
]
