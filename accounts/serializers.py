from rest_framework import serializers
from .models import Profile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class AccountStatsSerializer(serializers.Serializer):
    total_accounts = serializers.IntegerField()
    total_therapist_accounts = serializers.IntegerField()
    total_patient_accounts = serializers.IntegerField()
    therapist_no_e_psi = serializers.IntegerField()
    therapist_no_training = serializers.IntegerField()
    therapist_no_e_psi_training = serializers.IntegerField()
    therapists_by_platform = serializers.ListField(child=serializers.DictField())
    patient_by_age = serializers.ListField(child=serializers.DictField())
    patient_by_psyco = serializers.ListField(child=serializers.DictField())
