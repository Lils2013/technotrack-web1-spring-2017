from django.conf.urls import url
from . import views
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.BlogList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)$', views.OneBlog.as_view(), name='blog'),
]