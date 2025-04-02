from django.urls import path
from . import views

app_name = 'users_app'


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('home', views.home),
    path('login', views.login)
]