from django.urls import path
from . import views

urlpatterns = [
    path('new_calendar/', views.create_calendar_page, name='new_calendar'),
    path('calendar_list/', views.CalendarListView.as_view(), name='calendar_list'),
    path('find_therapist/', views.CalendarFindView.as_view(), name='find_therapist'),
    path('delete_calendar/<str:pk>', views.CalendarDeleteView.as_view(), name='delete_calendar'),
    path('update_calendar/<str:pk>', views.CalendarUpdateView.as_view(), name='update_calendar'),
]

htmx_urlpatterns = [
    path('create_calendar/', views.create_calendar, name='create_calendar'),
]

urlpatterns += htmx_urlpatterns
