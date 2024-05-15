import uuid
from django.db import models
from django.contrib.auth.models import User
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog
from ibge_data.models import UF, City


PLATFORMS = {
    'Whatsapp': 'Whatsapp',
    'Zoom': 'Zoom',
    'Google Meets': 'Google Meets',
    'Facetime': 'Facetime',
    'Microsoft Teams': 'Microsoft Teams',
    'Jitsi': 'Jitsi',
    'Outro': 'Outro',
}


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='accounts', null=True, blank=True)
    uf = models.ForeignKey(UF, on_delete=models.PROTECT, related_name='account', null=True, blank=True)
    history = AuditlogHistoryField()

    # patient user
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    complaint = models.TextField(null=True, blank=True)
    psychiatric = models.BooleanField(null=True, blank=True)
    emergency_number = models.CharField(max_length=20, null=True, blank=True)

    # therapist user
    crp = models.CharField(max_length=20, null=True, blank=True)
    platform = models.CharField(max_length=50, choices=PLATFORMS, null=True, blank=True)
    crp_check = models.BooleanField(null=True, blank=True)
    trained = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


auditlog.register(Profile)
