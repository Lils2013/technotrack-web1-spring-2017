from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Blog(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
