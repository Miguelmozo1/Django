from django.urls import path;
from . import views;

app_name = "master_app";

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/create/show', views.create_show),
    path('shows/add', views.add_show),
    path('shows/show/<int:id>', views.show),
    path('delete/show/<int:id>', views.delete_show),
    path('shows/edit/<int:id>', views.edit_show),
    path('update/show', views.update_show)
]