from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts_show/$', views.posts_show, name='posts_show'),
    url(r'^tags/(?P<tag_name>[a-zA-Z0-9_.-]+)/$', views.tag_detail, name='tag_detail'),
    url(r'^tags/$', views.tags_show, name='tags_show'),
    url(r'^tag/new/$', views.tag_new, name='tag_new'),
    url(r'^tag/(?P<tag_name>[a-zA-Z0-9_.-]+)/edit/$', views.tag_edit, name='tag_edit'), 
    url(r'^tag/(?P<tag_name>[a-zA-Z0-9_.-]+)/delete/$', views.tag_delete, name='tag_delete'),     
    url(r'^trips_show/$', views.trips_show, name='trips_show'),
    url(r'^trip/new/$', views.trip_new, name='trip_new'),
    url(r'^trip/(?P<slug>[\w-]+)/delete/$', views.trip_delete, name='trip_delete'),     
    url(r'^trip/(?P<slug>[\w-]+)/$', views.trip_detail, name='trip_detail'), 
    url(r'^trip/(?P<slug>[\w-]+)/edit/$', views.trip_edit, name='trip_edit'),     
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),    
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^photos/$', views.photos_show, name='photos_show'),
    url(r'^map/$', views.map, name='map'),
]
