from rest_framework import generics
from .serializers import TreatmentSerializer
from .models import Treatment
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class TreatmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)


class TreatmentRetrieveUppdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
