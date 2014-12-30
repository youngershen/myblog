#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.http import HttpResponse
from common.views.commonviews import Jinja2TemplateView
from .forms import ArticleForm
from .models import Article
from .models import Tag

class ArticleListView(Jinja2TemplateView):
    template_name='article_list.html'
    pass

class ArticleAddView(Jinja2TemplateView):
    template_name='article_add.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ArticleForm()
        context.update(dict(form=form))
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse(form.errors)


class ArticleDetailView(Jinja2TemplateView):
    pass
