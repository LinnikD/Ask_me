from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_me.views.home', name='home'),
    # url(r'^ask_me/', include('ask_me.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^ask_me/', include('ask.urls') ),
    url(r'^ask_me/$', 'ask.views.index' ),
)




if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )

