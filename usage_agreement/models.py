import uuid
from django.db import models
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField
from accounts.models import Profile


class UsageAgreementVersion(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    version = models.CharField(max_length=20)
    is_active = models.BooleanField()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.version


class UsageAgreement(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    version = models.ForeignKey(UsageAgreementVersion, on_delete=models.CASCADE, related_name='usageagreements')
    acceptance = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    history = AuditlogHistoryField()

    def __str__(self):
        return f'Versão aceita: {str(self.version)}'


auditlog.register(UsageAgreement)
auditlog.register(UsageAgreementVersion)
