from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from blog.models import Blog


class Post(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
