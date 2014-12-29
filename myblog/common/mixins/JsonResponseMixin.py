#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

class JsonResponseMixin(object):

    def render_to_json(self, context, **kwargs):
        json_obj = dict()
        json_boj.update(context, **kwargs)
        return JsonResponse(json_obj)

    def get(self, request, *args, **kwargs):

        context  = self.get_context_data(**kwargs);
        return self.render_to_json(context)
