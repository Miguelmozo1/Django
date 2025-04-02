from django.urls import path
from . import views

app_name = "course_app"

urlpatterns = [
    path('', views.index),
    path('new/course', views.create_course),
    path('delete/<int:id>', views.delete),
    path('erase/<int:id>', views.delete_course),
    path('comments/<int:id>', views.comments),
    path('create/comment/<int:id>', views.create_comment)
]