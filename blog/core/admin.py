# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model

from post.models import Post, Comment;


class PostInLine(admin.StackedInline):
    model = Post
    extra = 0

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'date_joined']
    inlines = [PostInLine, CommentInLine]

