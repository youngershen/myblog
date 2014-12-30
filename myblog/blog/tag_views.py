from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse

from common.views.commonviews import JsonView
from common.views.commonviews import Jinja2TemplateView
from .forms  import TagForm
from .models import Article
from .models import Tag


#logging
import logging
logger = logging.getLogger(__name__)
# Create your views here.

class TagJsonView(JsonView):

    def render_to_json(self, context, **kwargs):
        return JsonResponse('test', safe=False)

class TagListView(Jinja2TemplateView):
    pass


class TagAddJsonView(JsonView):

    def render_to_json(self, request, *args, **kwargs):
        form = TagForm(request.GET)
        if form.is_valid():
            form.save()
        return JsonResponse(request, safe=False)
    
    def post(self, request, *args, **kwargs):
        return Jsonresponse('hack')

class TagDetailView(Jinja2TemplateView):
    pass
