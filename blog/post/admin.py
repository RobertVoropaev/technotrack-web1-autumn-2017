# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from post.models import Post, Comment

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date_created']
    inlines = [CommentInLine]

@admin.register(Comment)
class CommetAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author', 'date_created']
