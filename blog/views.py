from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Propaganda
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    propagandas = Propaganda.objects.all().order_by('?')[:1]
    return render(request, 'blog/post_list.html', {'posts': posts, 'propagandas': propagandas})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    propagandas = Propaganda.objects.all().order_by('?')[:1]
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
        'propagandas': propagandas,
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

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.last_edited = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {
        'form': form,
        })

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.last_edited = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

