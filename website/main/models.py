from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    description = models.TextField(max_length=240)
    hours = models.PositiveSmallIntegerField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.activity + "\n" + self.description
