# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=123, max_length=255),
            preserve_default=False,
        ),
    ]