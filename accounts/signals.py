from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from usage_agreement.models import UsageAgreement, UsageAgreementVersion


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_user_usage_agreement(sender, instance, created, **kwargs):
    if created:
        version = UsageAgreementVersion.objects.get(is_active=True)
        UsageAgreement.objects.create(
            user=instance,
            version=version,
            acceptance=True
        )
