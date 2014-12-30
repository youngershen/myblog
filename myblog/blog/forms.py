#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from django.forms import ModelForm
from django.utils.translation import ugettext as _
from .models import Tag
from .models import Article 

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'icon', 'description']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags', 'category']
        error_messages={
                'title':{
                    'required':_('title is required'),
                    }
                }
