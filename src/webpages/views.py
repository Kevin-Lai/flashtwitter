from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>") # String of HTML code
	return render(request, "homepage.html", {})

def signin_view(request, *args, **kwargs):
	return render(request, "signin.html", {})

def signup_view(request, *args, **kwargs):
	return render(request, "signup.html", {})

def test_view(request, *args, **kwargs):
	test_context = {
		"test_text": "This is a test page",
		"test_list": [123, "Testing", 456]
	}
	return render(request, "testpage.html", test_context)
