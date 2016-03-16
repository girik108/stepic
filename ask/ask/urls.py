from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'qa.views.questions_new'),
    url(r'^login/$','qa.views.test'),
    url(r'^signup/$','qa.views.test'),
    url(r'^question/(?P<slug>\d+)/$','qa.views.question'),
    url(r'^ask/$','qa.views.test'),
    url(r'^(?P<pop>popular)/$','qa.views.questions_pop'),
    url(r'^new/$','qa.views.test'),
)
