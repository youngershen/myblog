#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from django.forms import ModelForm
from models import Tag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'icon', 'description']
