# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from post.models import *;
from django.views.generic import ListView, DetailView

class PostList(ListView):
    template_name = "post/post_all.html"
    model = Post

class PostDetail(DetailView):
    template_name = "post/post_id.html"
    model = Post
    pk_url_kwarg = "post_id"
