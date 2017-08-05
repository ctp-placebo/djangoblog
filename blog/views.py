from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from .models import Post, Propaganda

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    propagandas = Propaganda.objects.all().order_by('?')[:1]
    return render(request, 'blog/post_list.html', {'posts': posts, 'propagandas': propagandas})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        next_page = post.get_next_by_created_date()
    except Post.DoesNotExist:
        next_page = None
    try:
        prev_page = post.get_previous_by_created_date()
    except Post.DoesNotExist:
        prev_page = None
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'next_page': next_page,
        'prev_page': prev_page,
        })

""" need to add a function/method for propagandas that can be used by all views, else will have to repeat 2nd and partial 3rd lines of post_list #function to get the slogans on all pages.
def jam(propagandas):
    propagandas = Propaganda.objects.all().order_by('?')[:1]
    return propagandas
#cannot have 2 methods for same page/view, so this doeas not work, use classes
def header(request):
    propagandas = Propaganda.objects.all().order_by('?')[:1]
    return render(request, 'blog/post_list.html', {'propagandas':propagandas})
"""