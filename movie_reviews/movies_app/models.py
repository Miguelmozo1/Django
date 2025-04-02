from django.db import models
from users_app.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=45),
    user = models.ForeignKey(User, related_name='movies', on_delete = models.CASCADE, null=True)
    def __str__(self):
        return f'{self.title}'

class Director(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    movies = models.ManyToManyField(Movie, related_name='director')
    def __str__(self):
        return f'{self.director}'

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.review}'