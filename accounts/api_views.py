from rest_framework import generics, views, response, status
from django.db.models import Count, Avg
from .models import Profile
from .serializers import AccountSerializer, AccountStatsSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission


class AccountListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer


class AccountStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Profile.objects.all()

    def get(self, request):
        total_therapist_accounts = self.queryset.filter(crp__isnull=False).count()
        total_patient_accounts = self.queryset.filter(age__isnull=False).count()
        total_accounts = total_patient_accounts + total_therapist_accounts

        therapist_no_e_psi = self.queryset.filter(crp__isnull=False, e_psi__isnull=True, trained=True).count()
        therapist_no_training = self.queryset.filter(crp__isnull=False, e_psi__isnull=False, trained=False).count()
        therapist_no_e_psi_training = self.queryset.filter(crp__isnull=False, e_psi__isnull=True, trained=False).count()
        therapists_by_platform = self.queryset.filter(crp__isnull=False).values('platform').annotate(count=Count('id'))

        patient_by_age = self.queryset.filter(age__isnull=False).values('age').annotate(count=Count('id'))
        patient_by_psyco = self.queryset.filter(age__isnull=False).values('psychiatric').annotate(count=Count('id'))

        data = {
            'total_accounts': total_accounts,
            'total_therapist_accounts': total_therapist_accounts,
            'total_patient_accounts': total_patient_accounts,
            'therapist_no_e_psi': therapist_no_e_psi,
            'therapist_no_training': therapist_no_training,
            'therapist_no_e_psi_training': therapist_no_e_psi_training,
            'therapists_by_platform': therapists_by_platform,
            'patient_by_age': patient_by_age,
            'patient_by_psyco': patient_by_psyco,
        }
        serializer = AccountStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )
