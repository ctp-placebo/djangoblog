from django.shortcuts import render
from .models import Post, Propaganda

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    propagandas = Propaganda.objects.all().order_by('?')[:1]
    return render(request, 'blog/post_list.html', {'posts': posts, 'propagandas': propagandas})
