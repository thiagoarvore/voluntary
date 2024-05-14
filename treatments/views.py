from django.views.generic import CreateView, DeleteView
from .models import Treatment
from .forms import TreatmentModelForm
from django.shortcuts import get_object_or_404
from calendars.models import Calendar
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='login'), name='dispatch')
class TreatmentCreateView(CreateView):
    model = Treatment
    form_class = TreatmentModelForm
    template_name = 'patient/new_treatment.html'
    success_url = '/home/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        therapist_id = self.kwargs.get('therapist_id')
        schedule_id = self.kwargs.get('schedule_id')
        
        therapist = get_object_or_404(Profile, id=therapist_id)
        schedule = get_object_or_404(Calendar, id=schedule_id)
        
        context['therapist'] = therapist
        context['schedule'] = schedule
        context['is_active'] = True
        context['patient'] = self.request.user.profile
        return context

    def form_valid(self, form):
        therapist_id = self.kwargs.get('therapist_id')
        schedule_id = self.kwargs.get('schedule_id')
        therapist = get_object_or_404(Profile, id=therapist_id)
        schedule = get_object_or_404(Calendar, id=schedule_id)
        form.instance.therapist = therapist
        form.instance.schedule = schedule      
        form.instance.patient = self.request.user.profile
        form.instance.is_active = True
        return super().form_valid(form)
