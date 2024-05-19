from rest_framework import generics
from .serializers import TreatmentSerializer
from .models import Treatment


class TreatmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentRetrieveUppdateDestroyAPIView( generics.RetrieveUpdateDestroyAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
