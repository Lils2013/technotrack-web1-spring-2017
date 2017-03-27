from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from comment.models import Comment
from post.models import Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )


def add_comment(request, pk):
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
    return render(request, 'comment/addcomment.html', {'form': form})
