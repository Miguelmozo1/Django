from django.db import models
from master_app.models import User
from messages_app.models import Message

# Create your models here.

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['comment']) < 2:
            errors['comment'] = "Comment must be at least 2 characters"
        return errors


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showManager()
    def __str__(self):
        return f'Comment Obj: {self.id}'