from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa.views import test
from qa.views import home
from qa.views import popular
from qa.views import question
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls),name='home'),
    url(r'^$', home),
    url(r'^signup/?$', test),
    url(r'^question/(?P<id>\d+)',question),
    url(r'^ask/$',test),
    url(r'^(.+/)?popular/(\?page=\d\d?)?',popular),
    url(r'^new/$',test),
)
