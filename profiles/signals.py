""" provides comunications between User and Profile
    a sender (user) informs when an instance is createdto the receiver 
    (profile) 
    and a new profile instance should be also created automatically
"""
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
