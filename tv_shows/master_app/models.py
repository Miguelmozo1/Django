from django.db import models

# Create your models here.

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network description should be at least 3 characters"
        if len(postData['release_date']) < 1:
            errors["release_date"] = "release_date  should be at least 1 characters"
        if postData['description']:
            if len(postData['description']) < 10:
                errors["description"] = "Description should be at least 10 characters"

        # if len(postData['description']) < 10:
        #     errors["description"] = "Description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()
    def __str__(self):
        return f"Show:{self.id}, {self.title}, {self.network}, {self.release_date}, {self.description}"