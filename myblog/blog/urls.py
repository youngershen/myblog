from django.conf.urls import patterns
from django.conf.urls import url
from django.conf import settings
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # blog app
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^article/(?P<slug>[a-z0-9-]+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/$', ArticleListView.as_view(), name='article_list'),
    url(r'^tag/(?P<slug>[a-z0-9-]+)/$', TagDetailView.as_view(), name='tag_detail'),
    url(r'^tag/$', TagListView.as_view(), name='tag_list')
    )

