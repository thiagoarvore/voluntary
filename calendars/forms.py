from django import forms
from .models import Calendar


class CalendarModelForm(forms.ModelForm):

    class Meta:
        model = Calendar
        fields = ['week_day', 'schedule']
        widgets = {
            'week_day': forms.Select(attrs={'class': 'form-control'}),
            'schedule': forms.Select(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['week_day'].label = 'Dia da semana'
        self.fields['schedule'].label = 'Horário'
