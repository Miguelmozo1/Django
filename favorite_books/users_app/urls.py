from django.urls import path
from . import views


app_name = 'users_app'


urlpatterns = [
    path('register', views.register),
    path('login', views.login),
]