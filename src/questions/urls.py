from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^(?P<q_id>\d+)/$', views.get_question, name='get_question'),
    url(r'^$', views.index, name='index'),
    url(r'^ask_question$', views.ask_question, name='ask_question'),
    url(r'^save$', views.save, name='save'),
    url(r'^json_save$', views.json_save, name='json_save'),
    url(r'^json_get$', views.json_get, name='json_get'),
]
