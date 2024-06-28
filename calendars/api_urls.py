from django.urls import path
from . import api_views


urlpatterns = [
    path('calendars/', api_views.CalendarListCreateAPIView.as_view(), name='create_list_calendar'),
    path('calendar/<str:pk>/', api_views. CalendarRetrieveUpdateDestroyAPIView.as_view(), name='calendar_detail'),
    path('calendars/stats/', api_views.CalendarStatsView.as_view(), name='calendar_stats')
]
