# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-04-12 22:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_title', models.CharField(max_length=255, verbose_name='title')),
                ('tag_name', models.CharField(default=' ', max_length=30)),
                ('art_content', models.TextField()),
                ('art_img', models.ImageField(upload_to='static/img/')),
                ('art_status', models.CharField(choices=[('d', 'Drafts'), ('p', 'Published'), ('a', 'Approved')], default='d', max_length=1, verbose_name='publish status')),
                ('art_publish_date', models.DateTimeField(auto_now_add=True, verbose_name='publish date')),
                ('art_number_views', models.IntegerField(default=0, verbose_name='view count')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('art_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banword_name', models.CharField(max_length=255, verbose_name='BanWord')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment_content', models.TextField()),
                ('Comment_status', models.BooleanField(default=1, verbose_name='Is Approved')),
                ('Comment_parent_id', models.IntegerField(default=-1)),
                ('Comment_art_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('user_comment_like', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion_letter', models.CharField(max_length=255)),
                ('emotion_img', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_name', models.CharField(max_length=255)),
                ('keyword_art_id', models.ManyToManyField(to='articles.Article')),
            ],
        ),
        migrations.CreateModel(
            name='lockSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('article_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_img', models.ImageField(blank=True, upload_to=b'')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
