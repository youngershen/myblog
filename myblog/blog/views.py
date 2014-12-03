from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404

from common.mixins.Jinja2Mixins import Jinja2TemplateMixin
from .models import Article
from .models import Tag


#logging
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class IndexView(Jinja2TemplateMixin, TemplateView):
    template_name='base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context



#tag views
class TagListView(Jinja2TemplateMixin, TemplateView):
    template_name='index.html'

class TagDetailView(Jinja2TemplateMixin, TemplateView):
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



#article views
class ArticleListView(Jinja2TemplateMixin, TemplateView):
    template_name='article_list.html'

class ArticleDetailView(Jinja2TemplateMixin, TemplateView):
    template_name='index.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context.update(dict(**kwargs))
        slug = kwargs['slug']
        article = Article.objects.get(slug=slug)
        context.update(dict(aslug=article.get_absolute_url()))
        return context


class ArticleAddView(Jinja2TemplateMixin, TemplateView):
    template_name='article_add.html'

    def get(self, request, *args, **kwargs):
        context = dict()
        return self.render_to_response(context)
