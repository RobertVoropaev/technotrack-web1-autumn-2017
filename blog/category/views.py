# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from category.models import *;
from django.views.generic import ListView, DetailView

class CategoryList(ListView):
    template_name = "category/category_all.html"
    model = Category

class CategoryDetail(DetailView):
    template_name = "category/category_id.html"
    model = Category
    pk_url_kwarg = "category_id"
