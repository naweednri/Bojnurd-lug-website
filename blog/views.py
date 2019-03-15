from django.shortcuts import render, HttpResponse
from .models import Post, Comment, SubComment


def index(request):
    return render(request, 'index.html', {'posts': Post.objects.all()})

def post(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post.html', {'post': post})

def add_comment(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            post = Post.objects.get(id=request.POST['id'])
            post.comments.create(user=request.user, text=request.POST['text'])
    return HttpResponse('ok')