from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_note/$', views.new_note, name='new_note'),
    url(r'^new_link/$', views.new_link, name='new_link'),
    url(r'^new_photo/$', views.new_photo, name='new_photo'),
    url(r'^post_list/$', views.post_list, name='post_list'),
]