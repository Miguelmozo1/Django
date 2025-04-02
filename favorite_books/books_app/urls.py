from django.urls import path
from . import views


app_name = 'books_app'

urlpatterns = [
    path('create', views.create_book),
    path('<int:id>', views.book),
    path('update', views.update),
    path('add/<int:id>', views.add),
    path('remove/<int:id>', views.remove)
]