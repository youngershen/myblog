from django.conf.urls import patterns
from django.conf.urls import url
from django.conf import settings
from .views import *
from .tag_views import *
from .article_views import *
from .category_views import * 

urlpatterns = patterns('',
    # index
    url(r'^$', IndexView.as_view(), name='index'),
    #article url
    url(r'^article/$', ArticleListView.as_view(), name='article_list'),
    url(r'^article/add/$', ArticleAddView.as_view(), name='article_add'),
    url(r'^article/(?P<slug>[a-z0-9-]+)/$', ArticleDetailView.as_view(), name='article_detail'),
    #tag url
    url(r'^tag/$', TagListView.as_view(), name='tag_list'),
    url(r'^tag/add/$', TagAddJsonView.as_view(), name='tag_add_json_view'),
    url(r'^tag/(?P<slug>[a-z0-9-]+)/$', TagDetailView.as_view(), name='tag_detail'),
    )

