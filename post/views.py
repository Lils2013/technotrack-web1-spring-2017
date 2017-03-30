from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from comment.models import Comment
from .models import Post


class OnePost(generic.DetailView):
    template_name = 'post/one.html'
    queryset = Post.objects.all()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )


def one_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post:post', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post/one.html', {'form': form, 'object': post})


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
