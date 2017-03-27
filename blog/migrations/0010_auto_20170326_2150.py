# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0001_initial'),
        ('blog', '0009_blog_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(null=True, to='like.Like'),
        ),
    ]