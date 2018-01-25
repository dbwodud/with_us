from users.forms import *
from pytz import timezone
from datetime import datetime
from .models import User
from django.shortcuts import render
# Create your views here.

def signup(request):
	if request.method == 'POST':
		form = Form(request.POST)
		if form.is_valid():
			userprofile = Users()
			userprofile = form.save(commit=False)
			userprofile.user_jData = datetime.now(timezone('Asia/Seoul'))
			userprofile.save()
	else:
		form = Form()

	return render(request,'signup.html',{'form':form})