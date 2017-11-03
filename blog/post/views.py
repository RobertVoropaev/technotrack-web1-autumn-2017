# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from post.models import *;
from django.views.generic import ListView, DetailView
from django import forms


class PostList(ListView):
    template_name = "post/post_all.html"
    model = Post
    def get_queryset(self):
        q = super(PostList, self).get_queryset()
        self.form = PostListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        contex = super(PostList, self).get_context_data(**kwargs)
        contex["PostListForm"] = self.form
        return contex



class PostListForm(forms.Form):
    search = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(('title','title' ),
                                          ('-title', '-title'),
                                          ('date_create', 'date'),
                                          ('-date_create', '-date')),
                                 required=False)


class PostDetail(DetailView):
    template_name = "post/post_id.html"
    model = Post
    pk_url_kwarg = "post_id"
