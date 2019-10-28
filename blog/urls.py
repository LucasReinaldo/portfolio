from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:blog_id>', views.update, name='update'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('detail/<int:blog_id>/upvote', views.upvote, name='upvote'),
    path('search/', views.search_query, name='search'),
]
