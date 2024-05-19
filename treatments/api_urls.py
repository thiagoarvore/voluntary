from django.urls import path
from . import api_views


urlpatterns = [
    path('treatments/', api_views.TreatmentListCreateAPIView.as_view(), name='list_create_treatment'),
    path('treatment/<str:pk>', api_views.TreatmentRetrieveUppdateDestroyAPIView.as_view(), name='treatment_detail')
]