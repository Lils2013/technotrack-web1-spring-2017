from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'By ' + self.user.username
