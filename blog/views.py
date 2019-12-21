from django.shortcuts import render
from .models import Post


posts = Post.objects.all()


# Create your views here.
def home(request):
    # Instead of returning a simple HttpResponse, we are rendering the html template
    context = {'posts': posts, 'title': 'Spot'}
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context=None)
