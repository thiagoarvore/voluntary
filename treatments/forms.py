from django import forms
from .models import Treatment


class TreatmentModelForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ['therapist', 'patient', 'schedule', 'is_active']
