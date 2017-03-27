from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from comment.views import add_comment
from . import views

app_name = 'post'
urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.OnePost.as_view(), name='post'),
    url(r'^addpost/$', views.AddPost.as_view(), name='addpost'),
    url(r'^(?P<pk>\d+)/editpost/$', login_required(views.EditPost.as_view()), name='editpost'),
    url(r'^(?P<pk>\d+)/addcomment/$', login_required(add_comment), name='addcomment'),
]