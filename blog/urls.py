from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.post, name='post'),
    path('comment/', views.add_comment, name='add-comment')
]
