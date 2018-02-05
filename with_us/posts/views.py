from django.shortcuts import render , get_object_or_404 , redirect
from posts.forms import *
from .models import *

# Create your views here.
def index(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'posts/index.html',{'post':post})
	
def write(request):
	if request.method == 'POST':
		document = F_Document(request.POST)
		file_form = F_File(request.POST,request.FILES)

		if document.is_valid():
			files = request.FILES.getlist('file_path')
			post_data = M_Post()
			file_data = M_File()
			post_file = M_Post_File()
			post_data = document.save(commit=False)
			post_data.post_interests=0
			post_data.save()
			
			post_file.post = post_data

			for f in files:
				print(file_data)
				file_data.file_path = f
				file_data.save()
				post_file.file = file_data
				post_file.save()

			return redirect('../../')
	else:
		document = F_Document()
		file_form = F_File()
		
	return render(request,'write.html',{
		'Document':document,
		'File_from':file_form
		})

def post_modify(request):
	Postlist=M_Post.objects.all()
	return render(request,'posts/modify.html',{'Postlist':Postlist})
