from django import forms
from .models import Calendar


class CalendarModelForm(forms.ModelForm):

    class Meta:
        model = Calendar
        fields = ['week_day', 'schedule']

    widgets = {
        'week_day': forms.Select(),
        'schedule': forms.Select()
    }
