# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from category.models import *;
# Create your views here.


def show_category_all(request):
    return render(request, "category_all.html", {"categories": Category.objects.all()})

def show_category_id(request, category_id):
    category = get_object_or_404(Category.objects.all(), id=category_id)
    return render(request, "category_id.html", {"category": category})