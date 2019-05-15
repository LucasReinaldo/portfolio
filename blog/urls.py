from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='post_detail'),
    path('create', views.BlogCreate.as_view(), name='post_create'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='post_delete'),
    path('detail/<int:blog_id>/upvote', views.upvote, name='upvote'),
]
