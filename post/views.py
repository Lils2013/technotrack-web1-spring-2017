from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views import generic
from django.views.generic import DetailView

from comment.models import Comment
from like.models import Like
from .models import Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


def one_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return render(request, 'post/one.html',
                          {'form': CommentForm(), 'object': post, 'liked': post.like_set.filter(user=request.user)})
    else:
        form = CommentForm()
    return render(request, 'post/one.html',
                  {'form': form, 'object': post, 'liked': post.like_set.filter(user=request.user)})


class PostCommentsView(DetailView):

    queryset = Post.objects.all()
    template_name = "post/comments.html"


class PostLikeAjax(View):
    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post_object = get_object_or_404(Post, id=pk)
        return super(PostLikeAjax, self).dispatch(request, *args, **kwargs)

    def post(self,request):
        if not self.post_object.like_set.filter(user=self.request.user).exists():
            new_like, created = Like.objects.get_or_create(user=self.request.user,
                                                    post=self.post_object)
            new_like.save()
        return HttpResponse(Like.objects.filter(post=self.post_object).count())


class AddPost(generic.CreateView):
    template_name = 'post/addpost.html'
    model = Post
    fields = ('title', 'text', 'blog')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)

    def get_success_url(self):
        return reverse('post:post', args=(self.object.id,))


class EditPost(generic.UpdateView):
    template_name = 'post/editpost.html'
    model = Post
    fields = ('title', 'text')

    def get_queryset(self):
        return super(EditPost, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post:post', args=(self.object.id,))
