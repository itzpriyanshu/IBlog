from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def home(request):

    #load data
    post = Post.objects.all()[:11]
    print(post)

    data = {
        'posts': post
    }
    return render(request, 'index.html', data)

def post(request, url):
    post = Post.objects.get(url=url)
    print(post)
    return render(request, 'posts.html', {'post': post})