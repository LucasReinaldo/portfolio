from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<int:blog_id>/', views.post, name='post'),
    path('createpost/', views.createpost, name='createpost'),
    path('post/<int:blog_id>/upvote', views.upvote, name='upvote'),
]
