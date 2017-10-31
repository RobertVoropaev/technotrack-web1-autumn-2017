# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from core.models import *;

def show_main(request):
    return render(request, "base.html")

def show_user_all(request):
    return render(request, "user_all.html", {"users": User.objects.all()})

def show_user_id(request, user_id):
    user = get_object_or_404(User.objects.all(), id=user_id)
    return render(request, "user_id.html", {"user": user})


