# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from category.models import *;
from django.views.generic import ListView, DetailView
from django import forms


class CategoryDetail(DetailView):
    template_name = "category/category_id.html"
    model = Category
    pk_url_kwarg = "category_id"


class CategoryList(ListView):
    template_name = "category/category_all.html"
    model = Category

    def get_queryset(self):
        q = super(CategoryList, self).get_queryset()
        self.form = CategoryListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['CategoryListForm'] = self.form
        return context

class CategoryListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(('title', 'title'),
                                          ('title', 'title'),),
                                 required=False)
    search = forms.CharField(required=False)