from django .conf.urls import url
from django.views.generic import ListView, DetailView
from . import views
from blog.models import Post, Propaganda

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^$', views.header, name='header'),
]

