from django.conf.urls import url
from . import views

app_name = 'post'
urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.OnePost.as_view(), name='post'),
]