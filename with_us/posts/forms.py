from django import forms
from posts.models import *

class F_Document(forms.ModelForm):
	class Meta:
		model = M_Post
		fields=['post_contents']
		labels={
			'post_contents':'Contents',
		}

class F_File(forms.ModelForm):
	class Meta:
		model = M_File
		fields=['file_path']
		labels={
			'file_path':'files'
		}
		widgets={
			"file_path":forms.ClearableFileInput(attrs={'multiple':True})
		}
