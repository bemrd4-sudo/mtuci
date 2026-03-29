# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# тут все ссылки
urlpatterns = patterns('',
    url(r'^$', 'flatpages.views.home', name='home'),
    url(r'^hello/$', 'flatpages.views.home', name='home_duplicate'), 
    url(r'^static-page/$', 'flatpages.views.static_handler', name='static_page'),
    url(r'^admin/', include(admin.site.urls)),
)