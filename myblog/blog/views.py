from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from common.views.commonviews import Jinja2TemplateView
from .models import Article
from .models import Tag

#logging
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class IndexView(Jinja2TemplateView):
    template_name='base.html'
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context

