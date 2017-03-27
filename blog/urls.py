from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from blog.views import add_post
from . import views
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.BlogList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.OneBlog.as_view(), name='blog'),
    url(r'^addblog/$', login_required(views.AddBlog.as_view()), name='addblog'),
    url(r'^(?P<pk>\d+)/editblog/$', login_required(views.EditBlog.as_view()), name='editblog'),
    url(r'^(?P<pk>\d+)/addpost/$', login_required(add_post), name='addpost'),
]