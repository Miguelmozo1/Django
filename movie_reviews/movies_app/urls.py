from django.urls import path
from . import views

app_name = 'movies_app'

urlpatterns = [
    path('movie/add', views.add),
    path('movie/create', views.create),
    path('movie/<int:id>', views.movie),
]