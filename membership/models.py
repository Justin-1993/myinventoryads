from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Vip(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    is_vip = models.BooleanField(default=False)
    def __str__(self):
        user = str(self.user)
        return user

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Vip.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()