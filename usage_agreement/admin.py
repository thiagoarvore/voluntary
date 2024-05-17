from django.contrib import admin
from usage_agreement.models import UsageAgreementVersion, UsageAgreement


@admin.register(UsageAgreementVersion)
class UsageAgreementVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'version', 'is_active')


@admin.register(UsageAgreement)
class UFAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'version', 'acceptance', 'created_at')
