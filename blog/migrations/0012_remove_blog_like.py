# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170326_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='like',
        ),
    ]