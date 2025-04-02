from django.urls import path;
from . import views

app_name = "master_app"

urlpatterns = [
    path('', views.index),
    path('success', views.success),
    path('destroy', views.destroy)
]