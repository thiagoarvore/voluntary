from django.urls import path
from .views import TreatmentCreateView, EndTreatmentView, TreatmentTherapistListView

urlpatterns = [
    path('new_treatment/<str:therapist_id>/<str:schedule_id>', TreatmentCreateView.as_view(), name='new_treatment'),
    path('end_treatment/<str:pk>', EndTreatmentView.as_view(), name='end_treatment'),
    path('treatments/', TreatmentTherapistListView.as_view(), name='treatments')
]
