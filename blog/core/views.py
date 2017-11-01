# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from core.models import *;
from django.views.generic import ListView, TemplateView, DetailView

class MainTemplate(TemplateView):
    template_name = "core/base.html"

class UserList(ListView):
    template_name = "core/user_all.html"
    model = get_user_model() # settings.AUTH_USER_MODEL

class UserDetail(DetailView):
    model = get_user_model()
    template_name = "core/user_id.html"
    pk_url_kwarg = 'user_id'