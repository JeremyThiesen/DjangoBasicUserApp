from django.conf.urls import *

from user import views

urlpatterns = [
    url(r'^userlogin$', views.UserLogin, name='userlogin'),
    url(r'^logout$', views.UserLogout, name='logout'),
    
    url(r'^profile$', views.UserProfile, name='profile'),
]
