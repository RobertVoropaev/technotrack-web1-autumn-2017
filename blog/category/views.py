# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from django.shortcuts import reverse
from django.core.paginator import Paginator

from category.models import Category;

class CategoryDetail(DetailView):
    template_name = "category/category_detail.html"
    model = Category
    context_object_name = 'category'
    pk_url_kwarg = "category_id"


class CategoryListForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_by = forms.ChoiceField(choices=(('title', 'Title ASC'),
                                          ('-title', 'Ttitle DESC'),
                                          ('date_created', 'Date created ASC'),
                                          ('-date_created', 'Date created DESC')), widget=forms.Select(attrs={'class': 'form-control'}),
                                 required=False)
    page = forms.IntegerField(required=False)

class CategoryList(ListView):
    template_name = "category/category_all.html"
    model = Category
    categories_on_page = None

    def get_queryset(self):
        q = super(CategoryList, self).get_queryset()
        self.form = CategoryListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])

            if self.form.cleaned_data['page']:
                page_num = self.form.cleaned_data['page']
            else:
                page_num = 1
            self.categories_on_page = Paginator(q, 10).page(page_num)
        return q

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['CategoryListForm'] = self.form
        context['categories'] = self.categories_on_page
        return context



class CategoryCreate(CreateView):
    model = Category
    fields = ['title']
    template_name = 'category/category_create.html'

    def get_success_url(self):
        return reverse('category_detail', kwargs={'category_id': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CategoryCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(CategoryCreate, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        return form

class CategoryUpdate(UpdateView):
    model = Category
    fields = ['title']
    template_name = 'category/category_update.html'
    pk_url_kwarg = "category_id"

    def get_queryset(self):
        return super(CategoryUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse('category_detail', kwargs={'category_id': self.object.id})

    def get_form(self, form_class=None):
        form = super(CategoryUpdate, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        return form

