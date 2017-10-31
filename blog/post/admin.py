# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from post.models import *;

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'text'


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'text'