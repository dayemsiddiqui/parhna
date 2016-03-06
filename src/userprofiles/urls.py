from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'register', views.register, name='register'),
    url(r'profile/edit', views.editprofile, name='editprofile'),
    url(r'profile/getprofile', views.json_getprofile, name='getprofile'),
    url(r'profile/saveprofile', views.json_saveprofile, name='saveprofile'),
    url(r'profile', views.profile, name='profile'),
    url(r'login', views.signin, name='signin'),
    url(r'logout', views.signout, name='signout'),
]
