from django .conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import PropagandistSlogans

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', ListView.as_view(
        queryset=PropagandistSlogans.objects.all()[:2],
        template_name="blog/home.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=PropagandistSlogans,
        template_name="blog/home.html")),
]






"""
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-date")[:25],
        template_name="blog/blog.html")),

    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model=Post,
        template_name="blog/post.html")),
]
"""