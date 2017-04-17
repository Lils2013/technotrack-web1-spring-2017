from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from post.models import Post


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'By ' + self.user.username
