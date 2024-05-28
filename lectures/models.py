from django.db import models
from django.contrib.auth.models import User
# models.py
# Models define the structure of stored data.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
