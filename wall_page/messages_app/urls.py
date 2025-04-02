from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('create', views.create_message),
    path('delete', views.delete_message)
]