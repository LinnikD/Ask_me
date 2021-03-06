from django.conf.urls import patterns, include, url

from django.contrib.auth.views import login, logout



urlpatterns = patterns('',    

    url(r'^/', 'ask.views.index'),
	url(r'^ask/', 'ask.views.ask'),
    url(r'^login/$', login, {'template_name': 'registration/login.html', 'redirect_field_name': 'ask_me/login' }),
	url(r'^register/', 'ask.views.register', name='register' ),
    url(r'^logout/$', logout, {'next_page': 'ask_me/new' }),
	url(r'^question/(?P<question_id>\d+)$', 'ask.views.question', name='question'),
    url(r'^new/', 'ask.views.new', name='new'), 
	url(r'^user/(?P<u_id>\d+)$', 'ask.views.user', name='user'),
    url(r'^popular/', 'ask.views.popular', name='popular'), 
) 
