from django.shortcuts import render, HttpResponse
from .models import Post


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})

def post(request, post_id):
    return render(request, 'post.html', {'post': Post.objects.get(id=post_id)})