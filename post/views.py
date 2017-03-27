from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Post


class OnePost(generic.DetailView):
    template_name = 'post/one.html'
    queryset = Post.objects.all()


class AddPost(generic.CreateView):
    template_name = 'post/addpost.html'
    model = Post
    fields = ('title', 'text', 'blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)

    def get_success_url(self):
        return reverse('post:post',args=(self.object.id,))


class EditPost(generic.UpdateView):
    template_name = 'post/editpost.html'
    model = Post
    fields = ('title', 'text')

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post:post',args=(self.object.id,))