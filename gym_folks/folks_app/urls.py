from django.urls import path;
from . import views;

app_name = 'folks_app';

urlpatterns = [
    path('', views.root),
    path('gym/create', views.create_gym),
    path('folk/create', views.create_folk),
    path('delete/<int:id>', views.delete)
]