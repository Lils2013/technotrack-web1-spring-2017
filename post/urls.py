from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from comment.views import add_comment
from . import views

app_name = 'post'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.one_post, name='post'),
    url(r'^(?P<pk>\d+)/comments/$', views.PostCommentsView.as_view(), name='comments'),
    url(r'^addpost/$', login_required(views.AddPost.as_view()), name='addpost'),
    url(r'^(?P<pk>\d+)/editpost/$', login_required(views.EditPost.as_view()), name='editpost'),
    url(r'^(?P<pk>\d+)/addcomment/$', login_required(add_comment), name='addcomment'),
    url(r'^(?P<pk>\d+)/likeajax/$', login_required(views.PostLikeAjax.as_view()), name='likeajax'),
]