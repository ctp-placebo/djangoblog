from django .conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from blog.models import PropagandistSlogans

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]

"""
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
