from rest_framework import serializers
from .models import Treatment


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'


class TreatmentStatsSerializer(serializers.Serializer):
    total_treatments = serializers.IntegerField()
    treatments_by_week_day = serializers.ListField(child=serializers.DictField())
    treatments_by_hour = serializers.ListField(child=serializers.DictField())
    treatments_by_therapist = serializers.ListField(child=serializers.DictField())
    treatments_by_patient = serializers.ListField(child=serializers.DictField())
