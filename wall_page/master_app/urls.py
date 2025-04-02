from django.urls import path
from . import views

app_name = 'master_app'

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('home', views.home),
    path('destroy', views.destroy)
]