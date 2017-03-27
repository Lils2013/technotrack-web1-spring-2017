from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from like.models import Like


class Category(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        return 'Category: ' + self.title


class Blog(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category = models.ManyToManyField(Category)
    like = models.ManyToManyField(Like)

    def __unicode__(self):
        return 'Blog: ' + self.title
