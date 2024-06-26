from rest_framework import generics
from .models import Calendar
from .serializers import CalendarSerializer
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
