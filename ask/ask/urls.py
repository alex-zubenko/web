from django.conf.urls import patterns, include, url
from django.contrib import admin
#from qa.views import test
from qa.views import home, question, add_question, add_answer, login, popular, RegisterFormView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home,name='home'),
    #url(r'^signup/?$', register),
    url(r'^signup/?$', RegisterFormView.as_view()),
    url(r'^login/?$', login),
    url(r'^question/(\d+)/',question, name="question"),
    url(r'^ask/$',add_question),
    url(r'^answer/$',add_answer),
    url(r'^(.+/)?popular/(\?page=\d\d?)?',popular),
    #url(r'^new/$',test),
)
