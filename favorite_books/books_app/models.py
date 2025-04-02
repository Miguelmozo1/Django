from django.db import models
from users_app.models import User


# Create your models here.


class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "Title is required"
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least 5 characters"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    user = models.ForeignKey(User, related_name = "books", on_delete = models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
    def __str__(self):
        return f'{self.title}'