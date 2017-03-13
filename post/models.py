from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from blog.models import Blog

class Post(models.Model):

    blog = models.ForeignKey(Blog)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
