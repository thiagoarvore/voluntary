import uuid
from django.db import models
from accounts.models import Profile


WEEK_DAYS = {
    1: 'Segunda-feira',
    2: 'Terça-feira',
    3: 'Quarta-feira',
    4: 'Quinta-feira',
    5: 'Sexta-feira',
    6: 'Sábado',
    7: 'Domingo',
}

SCHEDULE_CHOICES = {
    4: '04:00',
    5: '05:00',
    6: '06:00',
    7: '07:00',
    8: '08:00',
    9: '09:00',
    10: '10:00',
    11: '11:00',
    12: '12:00',
    13: '13:00',
    14: '14:00',
    15: '15:00',
    16: '16:00',
    17: '17:00',
    18: '18:00',
    19: '19:00',
    20: '20:00',
    21: '21:00',
    22: '22:00',
    23: '23:00',
}


class Calendar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    therapist = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='calendars')
    week_day = models.PositiveSmallIntegerField(choices=WEEK_DAYS.items())
    schedule = models.PositiveSmallIntegerField(choices=SCHEDULE_CHOICES)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['week_day', 'schedule']

    def __str__(self):
        return f'{WEEK_DAYS[self.week_day]} - {self.get_schedule_display()}'
