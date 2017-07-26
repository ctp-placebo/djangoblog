from django.contrib import admin
from blog.models import Propaganda, Post 

# Register your models here.
# This makes the database editable from the admin panel. 
admin.site.register(Propaganda)
admin.site.register(Post)
