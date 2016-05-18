from django.conf.urls import url
from .import views	

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<question_id>[0-9]+)/$',views.detail, name = 'detail'),
	url(r'^(?P<question_id>[0-9]+/results)/$',views.results, name = 'results'),
	url(r'^(?P<question_id>[0-9]+/poll)/$',views.poll, name = 'poll'),
	url(r'^login/$', views.login, name = 'login'),
	url(r'^logout/$', views.logout, name = 'logout'),
	url(r'^auth_view/$', views.auth_view, name = 'auth_view'),
	url(r'^loggedin/$', views.loggedin, name = 'loggedin'),
	url(r'^invalid/$', views.invalid, name = 'invalid'),
]