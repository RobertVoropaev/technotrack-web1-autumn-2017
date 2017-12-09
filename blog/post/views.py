# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django import forms
from django.shortcuts import reverse, get_object_or_404

from post.models import Post, Comment;

class PostListForm(forms.Form):
    search = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices=(('title','Title ASC' ),
                                          ('-title', 'Title DESC'),
                                          ('date_created', 'Date created ASC'),
                                          ('-date_created', 'Date created DESC')),
                                 required=False)

class PostList(ListView):
    template_name = "post/post_all.html"
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        q = super(PostList, self).get_queryset().filter(isDeleted=False)
        self.form = PostListForm(self.request.GET)
        if self.form.is_valid():
            if self.form.cleaned_data['order_by']:
                q = q.order_by(self.form.cleaned_data['order_by'])
            if self.form.cleaned_data['search']:
                q = q.filter(title=self.form.cleaned_data['search'])
        return q

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context["PostListForm"] = self.form
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'text', 'categories']
    template_name = 'post/post_update.html'
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        return super(PostUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return reverse("post_detail", kwargs={'post_id': self.object.id})