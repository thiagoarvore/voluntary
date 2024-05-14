from django.urls import path
from .views import CalendarCreateView, CalendarListView, CalendarFindView

urlpatterns = [
    path('new_calendar/', CalendarCreateView.as_view(), name='new_calendar'),
    path('calendar_list/', CalendarListView.as_view(), name='calendar_list'),
    path('find_therapist/', CalendarFindView.as_view(), name='find_therapist')

]

urlpatternshtmx = [
]

urlpatterns += urlpatternshtmx