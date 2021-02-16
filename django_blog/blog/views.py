from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_message = "'%(title)s' created successfully"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_message(self, cleand_data):
        return self.success_message % dict(cleand_data, title=self.object.title)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_message = "'%(title)s' updated successfully"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
    def get_success_message(self, cleand_data):
        return self.success_message % dict(cleand_data, title=self.object.title)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog-home')
    success_message = "'%(title)s'  deleted successfully"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Blog | About'})
