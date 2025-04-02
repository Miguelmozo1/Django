from django.urls import path
from . import views

app_name = 'comments_app'


urlpatterns = [
    path('create/comment', views.create_comment)
]