from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
  path('post/new/', views.NewPostView.as_view(), name='post_new'),
  path('', views.BlogListView.as_view(), name='home'),
]
