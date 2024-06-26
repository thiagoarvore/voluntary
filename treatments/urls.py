from django.urls import path
from . import views

urlpatterns = [
    path('new_treatment/<str:therapist_id>/<str:schedule_id>/', views.treatment_create_view, name='new_treatment'),
    path('end_treatment/<str:pk>/', views.EndTreatmentView.as_view(), name='end_treatment'),
    path('treatments/', views.TreatmentListView.as_view(), name='treatments'),
    path('sending_mail/', views.sending_mail, name='sending_mail')
]

# htmx_urlpatterns = [
#     path('partial/new_treatment/<str:therapist_id>/<str:schedule_id>/', views.create_treatment, name='new_treatment_form')
# ]

# urlpatterns += htmx_urlpatterns
