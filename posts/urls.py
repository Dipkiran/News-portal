from django.conf.urls import url
from django.contrib import admin
from posts.views import posts_home

from posts.views import posts_create
from posts.views import posts_detail
from posts.views import post_list
from posts.views import posts_update
from posts.views import posts_delete

from . import views
urlpatterns = [

    url(r'^$',post_list, name= 'list'),
    url(r'^create/$',posts_create, name= 'posts_create'),
     url(r'^(?P<id>\d+)/$',posts_detail, name= 'detail'),
     url(r'^(?P<id>\d+)/edit/$',posts_update, name= ' update'),
     url(r'^(?P<id>\d+)/delete/$',posts_delete, name= 'posts_delete'),
]
