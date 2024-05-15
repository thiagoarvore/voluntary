from django.contrib import messages
from django.views.generic import CreateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CalendarModelForm
from .models import Calendar


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarCreateView(CreateView):
    model = Calendar
    form_class = CalendarModelForm
    template_name = 'therapist/new_calendar.html'
    
    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        # Antes de salvar o formulário, defina o usuário
        form.instance.therapist = self.request.user.profile
        messages.success(self.request, 'Seu horário foi disponibilizado com sucesso!')
        return super().form_valid(form)


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarListView(ListView):
    model = Calendar
    template_name = 'therapist/calendar_list.html'
    context_object_name = 'dates'
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(therapist=self.request.user.profile).order_by('week_day')
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarFindView(ListView):
    model = Calendar
    template_name = 'patient/find_therapist.html'
    context_object_name = 'options'

    def get_queryset(self):
        return Calendar.objects.filter(is_active=True)
