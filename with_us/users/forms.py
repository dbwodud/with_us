from django import forms
from users.models import *

class Form(forms.ModelForm):
	class Meta:
		model = User
		fields=['user_email','user_pw','user_gender','user_birthday']