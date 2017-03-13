from django.shortcuts import render
from django.views import generic
from .models import Blog
from post.models import Post
from comment.models import Comment


class BlogList(generic.ListView):
    template_name = 'blog/index.html'
    queryset = Blog.objects.all()


class OneBlog(generic.DetailView):
    template_name = 'blog/one.html'
    queryset = Blog.objects.all()


def blogcount(request):
    blog_list = Blog.objects.all()
    post_list = Post.objects.all()
    comment_list = Comment.objects.all()
    context = {'blog_list': blog_list, 'post_list': post_list, 'comment_list': comment_list}
    return render(request, 'blog/count.html', context)