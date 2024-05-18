from django.views.generic import CreateView, UpdateView, ListView
from .models import Treatment
from .forms import TreatmentModelForm
from django.shortcuts import get_object_or_404, redirect, render
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
        form.instance.therapist = therapist.id
        form.instance.schedule = schedule.id
        form.instance.patient = self.request.user.profile
        form.instance.is_active = True
        return super().form_valid(form)


def create_treatment(request, therapist_id, schedule_id):
    therapist = get_object_or_404(Profile, id=therapist_id)
    schedule = get_object_or_404(Calendar, id=schedule_id)
    print(therapist.id, schedule)
    if request.method == 'POST':
        form = TreatmentModelForm(request.POST)
        if form.is_valid():
            treatment = form.save(commit=False)
            treatment.therapist = therapist
            treatment.schedule = schedule
            treatment.patient = request.user.profile
            treatment.is_active = True
            treatment.save()
            return redirect('home')
    else:
        form = TreatmentModelForm()

    context = {
        'form': form,
        'therapist': therapist,
        'schedule': schedule,
        'is_active': True,
        'patient': request.user.profile
    }

    return render(request, 'patient/partials/new_treatment_form.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class TreatmentPartialCreateView(CreateView):
    model = Treatment
    form_class = TreatmentModelForm
    template_name = 'patient/partials/new_treatment_form.html'
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
