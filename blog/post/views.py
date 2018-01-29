# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from django.shortcuts import reverse, get_object_or_404
from django.core.paginator import Paginator

from post.models import Post, Comment;


class PostListForm(forms.Form):
    search = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    order_by = forms.ChoiceField(choices=(('title','Title ASC' ),
                                          ('-title', 'Title DESC'),
                                          ('date_created', 'Date created ASC'),
                                          ('-date_created', 'Date created DESC')), widget=forms.Select(attrs={'class': 'form-control'}),
                                 required=False)
    page = forms.IntegerField(required=False)


class PostList(ListView):
    template_name = "post/post_all.html"
    model = Post
    posts_on_page = None

    def get_queryset(self):
        q = super(PostList, self).get_queryset().filter(isDeleted=False)
        self.form = PostListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])

            if self.form.cleaned_data['page']:
                page_num = self.form.cleaned_data['page']
            else:
                page_num = 1
            self.posts_on_page = Paginator(q, 10).page(page_num)
        return q

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context["PostListForm"] = self.form
        context["posts"] = self.posts_on_page
        return context


class PostDetailAndCommentCreate(CreateView):
    model = Comment
    fields = ['text']

    template_name = 'post/post_detail.html'
    post_obj = Post.objects.all()[0]

    def dispatch(self, request, *args, **kwargs):
        self.post_obj = get_object_or_404(Post, id=kwargs['post_id'])
        return super(PostDetailAndCommentCreate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.post_obj.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.post_obj
        return super(PostDetailAndCommentCreate, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(PostDetailAndCommentCreate, self).get_form(form_class)
        form.fields['text'].widget = forms.Textarea(attrs={'class': 'form-control'})
        return form

    def get_context_data(self, **kwargs):
        context = super(PostDetailAndCommentCreate, self).get_context_data(**kwargs)
        context['post'] = self.post_obj
        return context


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'text', 'categories']
    template_name = 'post/post_create.html'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'post_id': self.object.id})

    def get_form(self, form_class=None):
        form = super(PostCreate, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['text'].widget = forms.Textarea(attrs={'class': 'form-control'})
        #Не отображается поле с выбором категории
        #form.fields['categories'].widget = forms.Select(attrs={'class': 'form-control'})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text', 'categories', 'isDeleted']
    template_name = 'post/post_update.html'
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse("post_detail", kwargs={'post_id': self.object.id})

    def get_form(self, form_class=None):
        form = super(PostUpdate, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        form.fields['text'].widget = forms.Textarea(attrs={'class': 'form-control'})
        #form.fields['categories'].widget = forms.TextInput(attrs={'class': 'form-control'})
        #плохо отображается Checkbox
        #form.fields['isDeleted'].widget = forms.Select(attrs={'class': 'form-control'})
        return form