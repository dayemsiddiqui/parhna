from django.conf.urls import include, url
#from django.contrib import admin

# from . import views

from .views import (
    index,
    post_detail,
    post_create,
    post_update,
    post_delete,
    view_category,
)

urlpatterns = [
    # Post urls
    url(r'^$', index),
    url(r'^(?P<id>\d+)/$', post_detail, name = 'detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name = 'update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete, name = 'delete'),
    url(r'^create/$', post_create),

    # Category urls
    url(r'^category/(?P<slug>[^\.]+)/$', view_category, name = 'view_post_category'),

]
