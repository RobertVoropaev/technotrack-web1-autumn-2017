# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from category.models import Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'
