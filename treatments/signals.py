from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Treatment
from calendars.models import Calendar
from datetime import datetime
from services.mail import Mail


@receiver(post_save, sender=Treatment)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        schedule_id = instance.schedule_id
        calendar = Calendar.objects.get(pk=schedule_id)
        calendar.is_active = False
        calendar.save()


@receiver(post_save, sender=Treatment)
def send_mail_event(sender, instance, created, **kwargs):
    if created:
        mail = Mail()
        schedule = instance.schedule
        therapist = instance.therapist
        therapist_whatsapp = therapist.whatsapp
        therapist_email = therapist.user.email
        patient = instance.patient
        patient_email = patient.user.email
        data = {
            'therapist': therapist,
            'therapist_email': therapist_email,
            'therapist_whatsapp': therapist_whatsapp,
            'patient': patient,
            'patient_email': patient_email,
            'schedule': schedule,
            'event_type': 'treatment_creation',
            'timestamp': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        }
        mail.send(data)
