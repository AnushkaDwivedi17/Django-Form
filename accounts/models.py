from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
