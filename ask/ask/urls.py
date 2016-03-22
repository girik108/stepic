from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^$', 'qa.views.questions_new', name = "main-page"),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name': 'login.html', 'redirect_field_name': "main-page"}),
    url(r'^signup/$','qa.views.signup'),
    url(r'^question/(?P<slug>\d+)/$','qa.views.question'),
    url(r'^ask/$','qa.views.ask'),
    url(r'^(?P<pop>popular)/$','qa.views.questions_pop'),
    url(r'^new/$','qa.views.ask'),
    url(r'^answer/$', 'qa.views.answer'),
)
