from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(M_Post)
admin.site.register(M_File)
admin.site.register(M_Post_File)