from django.urls import path
from .views import CalendarCreateView, CalendarListView, CalendarFindView, CalendarDeleteView, CalendarUpdateView

urlpatterns = [
    path('new_calendar/', CalendarCreateView.as_view(), name='new_calendar'),
    path('calendar_list/', CalendarListView.as_view(), name='calendar_list'),
    path('find_therapist/', CalendarFindView.as_view(), name='find_therapist'),
    path('delete_calendar/<str:pk>', CalendarDeleteView.as_view(), name='delete_calendar'),
    path('update_calendar/<str:pk>', CalendarUpdateView.as_view(), name='update_calendar'),
]
