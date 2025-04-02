from django.urls import path;
from . import views;

app_name = "master_app";

urlpatterns = [
    path('', views.index),
    path('destroy', views.reset),
    path('addtwo', views.two),
    path('custom', views.custom)
]