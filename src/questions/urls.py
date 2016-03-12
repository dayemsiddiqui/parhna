from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ask$', views.ask, name='ask'),
    url(r'^json_save$', views.json_save, name='json_save'),
    url(r'^json_get$', views.json_get, name='json_get'),
]
