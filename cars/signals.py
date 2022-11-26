from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ApplicationUser


@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ApplicationUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
# def save_profile(sender, instance, created, **kwargs):
#     user = instance
#     if created:
#         profile = Users(user=user)
#         profile.save()
