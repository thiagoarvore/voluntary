from .models import Treatment
from .forms import TreatmentModelForm
from calendars.models import Calendar
from accounts.models import Profile
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from sweetify.views import SweetifySuccessMixin


@login_required(login_url='login')
def sending_mail(request):
    return render(request, 'patient/partials/sending_mail.html')


@method_decorator(login_required(login_url='login'), name='dispatch')
class TreatmentCreateView(SweetifySuccessMixin, CreateView):
    model = Treatment
    form_class = TreatmentModelForm
    template_name = 'patient/new_treatment.html'
    success_url = reverse_lazy('home')


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
        self.object = form.save()
        return super().form_valid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class EndTreatmentView(UpdateView):
    model = Treatment
    form_class = TreatmentModelForm
    template_name = 'therapist/end_treatment.html'
    success_url = '/home/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        treatment = self.get_object()
        context['patient'] = treatment.patient
        context['schedule'] = treatment.schedule
        return context

    def form_valid(self, form):
        form.instance.is_active = False
        return super().form_valid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TreatmentListView(ListView):
    model = Treatment
    form_class = TreatmentModelForm
    template_name = 'treatments.html'
    context_object_name = 'options'
    success_url = '/treatments/'

    def get_queryset(self):
        if self.request.user.profile.crp:
            return Treatment.objects.filter(therapist=self.request.user.profile, is_active=True)
        if self.request.user.profile.age:
            return Treatment.objects.filter(patient=self.request.user.profile, is_active=True)
