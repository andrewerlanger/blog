from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models

# Create your views here.
class BlogListView(ListView):
  model = models.Post
  template_name = 'home.html'


class BlogDetailView(DetailView):
  model = models.Post
  template_name = 'post_detail.html'
