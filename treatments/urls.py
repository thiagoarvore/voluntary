from django.urls import path
from .views import TreatmentCreateView

urlpatterns = [
    path('new_treatment/<str:therapist_id>/<str:schedule_id>', TreatmentCreateView.as_view(), name='new_treatment')
]
