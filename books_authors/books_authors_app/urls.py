from django.urls import path;
from . import views;

app_name = "books_authors";

urlpatterns = [
    path('', views.root),
    path('authors', views.authors),
    path('book/<int:id>', views.book),
    path('author/<int:id>', views.author),
    path('add/book', views.create_book),
    path('create/author', views.create_author),
    path('join/author', views.join_author),
    path('join/book', views.join_book)
]