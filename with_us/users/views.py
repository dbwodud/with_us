from users.forms import *
from pytz import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.urls import reverse

# Create your views here.
def index(request):
	return render(request,'index.html')

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import SignupForm


def signup(request):
	signupform = SignupForm()
	if request.method == "POST":
		signupform = SignupForm(request.POST, request.FILES)
		if signupform.is_valid():
			print("true!")
			user = signupform.save(commit=False)
			user.email = signupform.cleaned_data['email']
            #user.avatar = signupform.clean_avatar()
			user.save()

			return HttpResponseRedirect(
			reverse("signin")
			)
	return render(request, "signup.html", {"signupform": signupform,})



def signin(request):
	if request.method == 'POST':
		signinform = AuthenticationForm(data=request.POST)
		if signinform.is_valid():
			username = signinform.cleaned_data.get('username')
			raw_password = signinform.cleaned_data.get('password')
			user = authenticate(request,username=username,password=raw_password)
			login(request,user)
			return redirect('../..')
		else:
			return redirect('../')
	else:
		signinform = AuthenticationForm()
	return render(request,'signin.html',{'signinform':signinform})

def my_comment(request):
	return render(request,'my_comment.html')

def my_posts(request):
	return render(request,'my_posts.html')

def profile(request):
	return render(request,'profile.html')

def bookmark(request):
	return render(request,'bookmark.html')

def modify(request):
	Userlist=User.objects.all()
	return render(request,'users/modify.html',{'Ul':Userlist})
