# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, reverse

from post.models import Post
from category.models import Category


def MainPageList(request):
    return render(request, 'core/main_page.html',
                  {'UserList': get_user_model().objects.order_by('-date_joined')[:3],
                   'PostList': Post.objects.order_by('-date_created')[:3],
                   'CategoryList': Category.objects.order_by('-date_created')[:3]})


class UserDetail(DetailView):
    model = get_user_model()
    template_name = "core/user_detail.html"
    context_object_name = 'object_user'
    pk_url_kwarg = 'user_id'


class UserListGetForm(forms.Form):
    search = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(('username', 'Name ASC'),
                                          ('-username', 'Name DESC'),
                                          ('date_joined', 'Date joined ASC'),
                                          ('-date_joined', 'Date joinded DESC')),
                                 required=False)


class UserList(ListView):
    template_name = "core/user_all.html"
    model = get_user_model()
    context_object_name = 'users'

    def get_queryset(self):
        q = super(ListView, self).get_queryset()
        self.form = UserListGetForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(username=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['UserListGetForm'] = self.form
        return context


class UserCreate(CreateView):
    model = get_user_model()
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = 'core/register.html'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'user_id': self.object.id})

    def form_valid(self, form):
        form.instance.set_password(form.instance.password)
        return super(UserCreate, self).form_valid(form)


class UserUpdate(UpdateView):
    model = get_user_model()
    fields = ['username', 'first_name', 'last_name', 'email']
    template_name = 'core/user_update.html'
    pk_url_kwarg = 'user_id'

    def get_success_url(self):
        return reverse('user_detail', kwargs={'user_id': self.object.id})

    def get_queryset(self):
        return super(UserUpdate, self).get_queryset().filter(username=self.request.user.username)
