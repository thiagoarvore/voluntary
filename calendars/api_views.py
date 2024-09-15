from rest_framework import generics, views, response, status
from django.db.models import Count
from .models import Calendar
from .serializers import CalendarSerializer, CalendarStatsSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission


class CalendarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)


class CalendarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)


class CalendarStatsView(views.APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Calendar.objects.all()

    def get(self, request):
        calendars = self.queryset
        total_calendars = calendars.count()
        total_active_calendars = calendars.filter(is_active=True).count()
        calendars_by_week_day = self.queryset.values('week_day').annotate(count=Count('id'))
        calendars_by_hour = self.queryset.values('schedule').annotate(count=Count('id'))
        calendars_by_therapist = self.queryset.values('therapist__name').annotate(count=Count('id'))

        data = {
            'calendars': calendars,
            'total_calendars': total_calendars,
            'total_active_calendars': total_active_calendars,
            'calendars_by_week_day': calendars_by_week_day,
            'calendars_by_hour': calendars_by_hour,
            'calendars_by_therapist': calendars_by_therapist,
        }
        serializer = CalendarStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
