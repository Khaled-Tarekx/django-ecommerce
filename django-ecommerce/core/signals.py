from .models import UserProfile
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
