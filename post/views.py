from django.shortcuts import render
from django.views import generic
from .models import Post


class OnePost(generic.DetailView):
    template_name = 'post/one.html'
    queryset = Post.objects.all()
