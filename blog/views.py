from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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


class EditBlog(generic.UpdateView):
    template_name = 'blog/editblog.html'
    model = Blog
    fields = ('title', 'description', 'category')
    success_url = '/blogs/'

    def get_queryset(self):
        return super(EditBlog, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('blog:blog',args=(self.object.id,))


class AddBlog(generic.CreateView):
    template_name = 'blog/addblog.html'
    model = Blog
    fields = ('title', 'description', 'category')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddBlog, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog',args=(self.object.id,))


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', )


def add_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.blog = blog
            post.author = request.user
            post.save()
            return redirect('post:post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/addpost.html', {'form': form})


def blogcount(request):
    blog_list = Blog.objects.all()
    post_list = Post.objects.all()
    comment_list = Comment.objects.all()
    context = {'blog_list': blog_list, 'post_list': post_list, 'comment_list': comment_list}
    return render(request, 'blog/count.html', context)