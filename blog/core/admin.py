# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from core.models import *;
from django.contrib import admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email'

