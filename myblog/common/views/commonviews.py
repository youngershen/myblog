#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.base import ContextMixin
from common.mixins.commonmixins import Jinja2ResponseMixin
from common.mixins.commonmixins import JsonResponseMixin

class Jinja2TemplateView(Jinja2ResponseMixin, TemplateView):
    pass

class JsonView(JsonResponseMixin, ContextMixin, View):
    pass
