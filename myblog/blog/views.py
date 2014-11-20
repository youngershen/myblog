from django.shortcuts import render
from django.views.generic import TemplateView
from common.mixins.Jinja2Mixins import Jinja2TemplateMixin
from blog.models import Article
from blog.models import Tag
from django.http import Http404

#logging
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class IndexView(Jinja2TemplateMixin, TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update(dict(name='sss'))
        logger.info("=========================")
        return context


class TagListView(TemplateView):
    template_name='index.html'

class TagDetailView(TemplateView):
    template_name='index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context.update(dict(**kwargs))
        slug = kwargs['slug']
        try:
            tag = Tag.objects.get(slug=slug)
        except Tag.DoesNotExist as e:
            raise Http404
        else:
            context.update(dict(aslug=tag.get_absolute_url()))
            return context


class ArticleListView(TemplateView):
    template_name='index.html'


class ArticleDetailView(TemplateView):
    template_name='index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context.update(dict(**kwargs))
        slug = kwargs['slug']
        article = Article.objects.get(slug=slug)
        context.update(dict(aslug=article.get_absolute_url()))
        return context
