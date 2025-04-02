from django.db import models

# Create your models here.

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Name of course must be greater than 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Description must be greater than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
    def __str__(self):
        return f'Course Obj: id:{self.id}, name:{self.name}'
    
class Description(models.Model):
    description = models.CharField(max_length=400)
    course = models.OneToOneField(Course, related_name='description' ,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Description Obj: {self.description}'
    

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'Comment Obj: {self.id}, {self.comment}, {self.course}'
