from django.shortcuts import render
from django.views.generic import TemplateView
from common.mixins.Jinja2Mixins import Jinja2TemplateMixin
# Create your views here.

class IndexView( TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(dict(name='sss'))
        return context
