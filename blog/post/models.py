# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from category.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="posts",)
    categories = models.ManyToManyField(Category, related_name="posts")

    isDeleted = models.BooleanField(default=False);

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    text = models.TextField()

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comments")
    post = models.ForeignKey(Post, related_name="comments")

    def __str__(self):
        return self.text
    class Meta:
        ordering = ['date_created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'