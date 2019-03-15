from django.db import models
from django.contrib.auth.models import User


class PostImage(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # please add a location field to this
    date = models.DateField()  # when is the event
    unitl = models.DateField()  # when singup for the event finishes

    def __str__(self):
        return self.title


class SubComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=60)

    def __str__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=60)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    subcomments = models.ManyToManyField(SubComment)

    def __str__(self):
        return self.text


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(PostImage)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
