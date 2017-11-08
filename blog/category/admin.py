# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from category.models import Category
from post.models import Post

class PostInLine(admin.TabularInline):
    model = Post
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    #inlines = [PostInLine]