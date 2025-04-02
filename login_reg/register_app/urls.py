from django.urls import path
from . import views

app_name = "register_app"

urlpatterns = [
    path('register/user', views.register),
]