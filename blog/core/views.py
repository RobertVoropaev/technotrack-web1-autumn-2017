# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django import forms
from django.shortcuts import render
from post.models import Post
from category.models import Category


class UserDetail(DetailView):
    model = get_user_model()
    template_name = "core/user_id.html"
    pk_url_kwarg = 'user_id'

class UserList(ListView):
    template_name = "core/user_all.html"
    model = get_user_model()

    def get_queryset(self):
        q = super(ListView, self).get_queryset()
        self.form = UserListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(username=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['UserListForm'] = self.form
        return context

class UserListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(('username', 'name'),
                                          ('-username', '-name'),
                                          ('date_joined', 'date'),
                                          ('-date_joined', '-date')),
                                 required=False)
    search = forms.CharField(required=False)


#add ordering by popular
def MainPageList(request):
    return render(request, 'core/main_page.html',
                  {'UserList': get_user_model().objects.all()[:3],
                   'PostList': Post.objects.all()[:3],
                   'CategoryList': Category.objects.all()[:3]})