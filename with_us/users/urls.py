from django.conf.urls import url
from users.views import *
urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^signup/$',signup,name='signup'),
	url(r'^signin/$',signin,name='signin'),
	url(r'^profile/$',profile,name='profile'),
	url(r'^my_posts/$',my_posts,name='my_posts'),
	url(r'^my_comment/$',my_comment,name='my_comment'),
	url(r'^bookmark/$',bookmark,name='bookmark'),
	url(r'^modify/$',modify,name='posts_modify'),
]
