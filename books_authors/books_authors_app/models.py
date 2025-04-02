from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"Book Obj: {self.id}, {self.title}, {self.description}"


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(max_length = 255, null=True)
    books = models.ManyToManyField(Book, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __str__(self):
        return f"Author Obj: {self.id} ,{self.first_name}, {self.last_name} , {self.notes}, {self.books}"