from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Treatment
from calendars.models import Calendar


@receiver(post_save, sender=Treatment)
def create_user_profile(sender, instance, created, **kwargs):
    if created:        
        schedule_id = instance.schedule_id
        calendar = Calendar.objects.get(pk=schedule_id)
        print(calendar.is_active)
        calendar.is_active = False
        print(calendar.is_active)
        calendar.save()