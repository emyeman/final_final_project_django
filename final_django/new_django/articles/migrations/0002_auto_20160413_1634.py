# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-13 16:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user_comment_like',
            new_name='Comment_user_like',
        ),
    ]
