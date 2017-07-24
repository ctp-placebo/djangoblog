from django.contrib import admin
from blog.models import PropagandistSlogans, Post

# Register your models here.
# This makes the database editable from the admin panel. 
admin.site.register(PropagandistSlogans)
admin.site.register(Post)
