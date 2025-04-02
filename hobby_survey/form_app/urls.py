from django.urls import path;
from . import views;

app_name = "form_app";

urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('show', views.show)
]