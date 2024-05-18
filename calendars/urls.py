from django.urls import path
from . import views

urlpatterns = [
    path('new_calendar/', views.create_calendar_page, name='new_calendar'),
    path('calendar_list/', views.CalendarListView.as_view(), name='calendar_list'),
    path('find_therapist/', views.CalendarFindView.as_view(), name='find_therapist'),
    path('delete_calendar/<str:pk>', views.delete_calendar, name='delete_calendar'),
    path('update_calendar/<str:pk>', views.update_calendar, name='update_calendar'),
]

htmx_urlpatterns = [
    path('create_calendar/', views.create_calendar, name='create_calendar'),
    path('partial_calendar_list/', views.CalendarPartialListView.as_view(), name='partial_calendar_list')
]

urlpatterns += htmx_urlpatterns
