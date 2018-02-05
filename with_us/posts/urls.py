from django.conf.urls import url
from posts.views import *

urlpatterns = [
	url(r'^(?P<pk>\d+)/$',index,name='post_detail'),
	url(r'^write/$',write,name='write'),
	url(r'^modify/$',post_modify,name='modify'),
]
