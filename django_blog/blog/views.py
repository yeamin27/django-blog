from django.shortcuts import render

def index(request):
    posts = [
        {
            'author': 'John Doe',
            'title': 'Test Title 1',
            'content': 'First blog post.',
            'date_posted': 'January 08, 2021'
        },
        {
            'author': 'Doe John',
            'title': 'Test Title 2',
            'content': 'Second blog post.',
            'date_posted': 'January 12, 2021'
        }
    ]
    context = {
        'posts': posts,
        'title' : 'Blog | Home'
    }
    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'Blog | About'})