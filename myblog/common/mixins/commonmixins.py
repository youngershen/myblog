#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

from django.http import JsonResponse
from coffin.template.response import TemplateResponse

class Jinja2ResponseMixin(object):
    response_class = TemplateResponse

class JsonResponseMixin(object):

    def render_to_json(self, request, *args, **kwargs):
        json_obj = dict()
        json_obj.update(request, **kwargs)
        return JsonResponse(json_obj)

    def get(self, request, *args, **kwargs):
        return self.render_to_json(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.render_to_json(request, *args, **kwargs)
