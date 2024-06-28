from rest_framework import generics, views, response, status
from django.db.models import Count
from .serializers import TreatmentSerializer, TreatmentStatsSerializer
from .models import Treatment
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission


class TreatmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)


class TreatmentRetrieveUppdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)


class TreatmentStatsView(views.APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Treatment.objects.all()

    def get(self, request):
        treatments = self.queryset
        total_treatments = treatments.count()
        treatments_by_week_day = self.queryset.values('week_day').annotate(count=Count('id'))
        treatments_by_hour = self.queryset.values('schedule').annotate(count=Count('id'))
        treatments_by_therapist = self.queryset.values('therapist__name').annotate(count=Count('id'))
        treatments_by_patient = self.queryset.values('patient__name').annotate(count=Count('id'))


        data = {
            'treatments': treatments,
            'total_treatments': total_treatments,
            'treatments_by_week_day': treatments_by_week_day,
            'treatments_by_hour': treatments_by_hour,
            'treatments_by_therapist': treatments_by_therapist,
            'treatments_by_patient': treatments_by_patient,
        }
        serializer = TreatmentStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
