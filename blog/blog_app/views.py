from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'mariele',
        'title': 'blog post 1',
        'content': 'my content',
        'date': '14 Sept 2023'
    },

    {
        'author': 'Lola',
        'content': 'her content',
        'date': '13 Sept 2023'
    }
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog_app/home.html', context)


def about(request):
    return render(request, 'blog_app/about.html', {'title': 'About'})