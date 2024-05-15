import uuid
from django.db import models
from accounts.models import Profile
from calendars.models import Calendar

# Create your models here.
class Treatment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    patient = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='patient_treatments')
    therapist = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='therapist_treatments')
    schedule = models.ForeignKey(Calendar, on_delete=models.CASCADE, related_name='treatments')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.patient} em tratamento com {self.therapist} - {self.schedule}'
