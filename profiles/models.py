""" defines user profile model containig:
    user one profile per each one, bio, avatar,created, updated
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio =  models.TextField(default="no bio...")
    avatar = models.ImageField(upload_to='avatars', default='no_picture.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"profile of {self.user.username}"

