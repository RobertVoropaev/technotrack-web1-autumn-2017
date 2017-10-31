# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from post.models import *;

# Create your views here.


def show_post_all(request):
    return render(request, "post_all.html", {"posts": Post.objects.all()})

def show_post_id(request, post_id):
    post = get_object_or_404(Post.objects.all(), id=post_id)
    return render(request, "post_id.html", {"post": post})