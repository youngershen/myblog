#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from coffin.template.response import TemplateResponse

class Jinja2TemplateMixin(object):
    response_class = TemplateResponse
