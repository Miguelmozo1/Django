from django.urls import path
from . import views

app_name = "game_app";

urlpatterns = [
    path('', views.root),
    path('index', views.index),
    path('guess', views.attempt),
    path('reset', views.reset),
    path('lose', views.lost)
]