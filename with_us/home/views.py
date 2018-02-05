from django.shortcuts import render
from posts.forms import *
from posts.models import M_Post

# Create your views here.

def index(request):

	Postlist=M_Post.objects.order_by('-post_no').all()

	return render(request,'home/index.html',{'Postlist':Postlist})