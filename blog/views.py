from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Ayoola Dogo',
        'title': 'Python developer available',
        'content': 'First post content',
        'posted_date': 'December 19, 2019',
    },
    {
        'author': 'John Doe',
        'title': 'Second blog post',
        'content': 'Second post content - Great content',
        'posted_date': 'December 20, 2019',
    },
]


# Create your views here.
def home(request):
    # Instead of returning a simple HttpResponse, we are rendering the html template
    context = {'posts': posts, 'title': 'Spot'}
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context=None)
