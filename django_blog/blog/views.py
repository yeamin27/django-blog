from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

def index(request):
    context = {
        'posts': Post.objects.all(),
        'title' : 'Blog | Home'
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'Blog | About'})
