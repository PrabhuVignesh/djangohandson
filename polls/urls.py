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
	url(r'^name/(?P<name>[a-z\-]+)/$',views.name, name = 'name'),
	url(r'^register/$',views.register, name='register'),
	url(r'^register_ack/$', views.register_ack, name = 'register_ack'),
	url(r'^post_create/$', views.post_create, name = 'post_create'),
	url(r'^post_list/$', views.post_list, name = 'post_list'),
	url(r'^likes/(?P<post_id>\d+)/$', views.like, name = 'like'),


]