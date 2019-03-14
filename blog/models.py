from django.db import models
from django.contrib.auth.models import User


class PostImage(models.Model):
    title = models.CharField(max_length=15)
    image = models.ImageField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(PostImage)

    def __str__(self):
        return self.title
