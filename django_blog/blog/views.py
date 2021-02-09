from django.shortcuts import render
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all(),
        'title' : 'Blog | Home'
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Blog | About'})