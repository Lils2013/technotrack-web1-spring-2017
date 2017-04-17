from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from post.models import Post


class Comment(models.Model):

    post = models.ForeignKey(Post)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return 'Comment: ' + self.text
