# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.

def show_post_all(request):
    return render(request, "post_all.html")

def show_post_id(request, post_id):
    return render(request, "post_id.html", {"post_id": post_id})

def show_user_all(request):
    return render(request, "user_all.html")

def show_user_id(request, user_id):
    return render(request, "user_id.html", {"user_id": user_id})


