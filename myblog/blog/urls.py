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
)

