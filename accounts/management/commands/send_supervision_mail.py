from accounts.models import Profile
from services.mail import Mail
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        therapists = [person.user.email for person in Profile.objects.filter(crp__isnull=False)]
        mail = Mail()
        mail.send_supervision_mail(therapists)
