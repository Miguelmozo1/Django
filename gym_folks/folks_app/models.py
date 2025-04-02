from django.db import models

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 2)
    def __str__(self):
        return f"Gym object: {self.id}, {self.name}, {self.city}, {self.state}"

class Folks(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    gym = models.ForeignKey(Gym, related_name='folks', on_delete = models.CASCADE)
    def __str__(self):
        return f"Folk object: {self.id}, {self.first_name}, {self.last_name}, {self.gym}"