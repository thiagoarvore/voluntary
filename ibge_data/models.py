from django.db import models

# Create your models here.
import uuid
from django.db import models


class UF(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    UF = models.ForeignKey(UF, on_delete=models.PROTECT, related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
