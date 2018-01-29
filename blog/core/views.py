# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, reverse
from django.core.paginator import Paginator

from post.models import Post
from category.models import Category


def MainPageList(request):
    return render(request, 'core/main_page.html',
                  {'UserList': get_user_model().objects.order_by('-date_joined')[:1],
                   'PostList': Post.objects.order_by('-date_created')[:1],
                   'CategoryList': Category.objects.order_by('-date_created')[:1]})


class UserDetail(DetailView):
    model = get_user_model()
    template_name = "core/user_detail.html"
    context_object_name = 'object_user'
    pk_url_kwarg = 'user_id'


class UserListGetForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_by = forms.ChoiceField(choices=(('username', 'Name ASC'),
                                          ('-username', 'Name DESC'),
                                          ('date_joined', 'Date joined ASC'),
                                          ('-date_joined', 'Date joinded DESC')), widget=forms.Select(attrs={'class': 'form-control'}),
                                 required=False)
    page = forms.IntegerField(required=False)


class UserList(ListView):
    template_name = "core/user_all.html"
    model = get_user_model()
    users_on_page = None

    def get_queryset(self):
        q = super(ListView, self).get_queryset()
        self.form = UserListGetForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(username=self.form.cleaned_data['search'])
            if self.form.cleaned_data['page']:
                page_num = self.form.cleaned_data['page']
            else:
                page_num = 1
            self.users_on_page = Paginator(q, 10).page(page_num)
        return q

    def get_context_data(self, **kwargs):
        context = super(UserList, self).get_context_data(**kwargs)
        context['UserListGetForm'] = self.form
        context['users'] = self.users_on_page
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

    def get_form(self, form_class=None):
        form = super(UserUpdate, self).get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control'})
        return form
