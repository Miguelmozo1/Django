from django.urls import path;
from . import views;

app_name = "gold_collector";

urlpatterns = [
    path('', views.root),
    path('gold', views.gold),
    path('reset', views.reset)
]