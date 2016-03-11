from django.conf.urls import patterns, include, url
from django.contrib import admin
from qa.views import home, question, add_question, add_answer, do_login, popular, register

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home,name='home'),
    url(r'^signup/?$', register),
    url(r'^register/?$', register),
    url(r'^login/?$', do_login),
    url(r'^question/(\d+)/',question, name="question"),
    url(r'^ask/$',add_question),
    url(r'^answer/$',add_answer),
    url(r'^(.+/)?popular/(\?page=\d\d?)?',popular),
)
