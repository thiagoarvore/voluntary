from rest_framework import serializers
from .models import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = '__all__'


class CalendarStatsSerializer(serializers.Serializer):
    total_calendars = serializers.IntegerField()
    calendars_by_week_day = serializers.ListField(child=serializers.DictField())
    calendars_by_hour = serializers.ListField(child=serializers.DictField())
    calendars_by_therapist = serializers.ListField(child=serializers.DictField())
