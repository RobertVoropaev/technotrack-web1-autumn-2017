# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from category.models import *;
from django.conf import settings;


class Post(models.Model):
    title = models.CharField(max_length=255, default="default_title")
    text = models.TextField(default="default_text")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="posts") #Почему нельзя без Null
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="posts")
    class Meta:
        ordering = ["-date_create"]


class Comment(models.Model):
    text = models.TextField(default="default_comment")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="comments")
    post = models.ForeignKey(Post, null=True, related_name="comments")
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
