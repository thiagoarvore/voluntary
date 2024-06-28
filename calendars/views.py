from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import CalendarModelForm
from .models import Calendar


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarListView(ListView):
    model = Calendar
    template_name = 'therapist/calendar_list.html'
    context_object_name = 'dates'

    def get_queryset(self):
        queryset = Calendar.objects.filter(therapist=self.request.user.profile)
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarPartialListView(ListView):
    model = Calendar
    template_name = 'therapist/partials/partial_calendar_list.html'
    context_object_name = 'dates'

    def get_queryset(self):
        queryset = Calendar.objects.filter(therapist=self.request.user.profile)
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarFindView(ListView):
    model = Calendar
    template_name = 'patient/find_therapist.html'
    context_object_name = 'options'

    def get_queryset(self):
        queryset = Calendar.objects.filter(is_active=True).select_related('therapist')
        search_therapist = self.request.GET.get('search_therapist')
        search_week_day = self.request.GET.get('search_week_day')
        if search_therapist:
            queryset = queryset.filter(therapist__name__icontains=search_therapist)
        if search_week_day:
            if search_week_day == '0':
                queryset = Calendar.objects.filter(is_active=True)
            else:
                queryset = queryset.filter(week_day=search_week_day)
        return queryset


@method_decorator(login_required(login_url='login'), name='dispatch')
class CalendarUpdateView(UpdateView):
    model = Calendar
    form_class = CalendarModelForm
    template_name = 'therapist/update_calendar.html'
    success_url = '/home/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = self.get_object()
        context['week_day_name'] = date.get_week_day_display()
        context['schedule_name'] = date.get_schedule_display()
        return context

    def form_valid(self, form):
        form.instance.is_active = True
        return super().form_valid(form)


@login_required(login_url='login')
def create_calendar(request):
    if request.method == 'POST':
        form = CalendarModelForm(request.POST)
        calendar = form.save(commit=False)
        if Calendar.objects.filter(therapist=request.user.profile, week_day=calendar.week_day, schedule=calendar.schedule).exists():
            return render(request, 'therapist/partials/calendar.html', context={'failed': 'failed'})
        if form.is_valid():            
            calendar.therapist = request.user.profile
            calendar.save()
            return render(request, 'therapist/partials/calendar.html')
    return render(request, 'therapist/partials/new_calendar_form.html', {'form': CalendarModelForm(), 'success': 'success'})


@login_required(login_url='login')
def create_calendar_page(request):
    form = CalendarModelForm()
    context = {
        'form': form,
        'calendar': Calendar.objects.filter(therapist=request.user.profile)
    }
    return render(request, 'therapist/new_calendar.html', context)


@login_required(login_url='login')
def delete_calendar(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        calendar.delete()
        queryset = Calendar.objects.filter(therapist=request.user.profile).order_by('week_day')
        context = {'dates': queryset}
        return render(request, 'therapist/partials/partial_calendar_list.html', context)

    return render(request, 'therapist/delete_calendar.html', {'calendar': calendar})


@login_required(login_url='login')
def update_calendar(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        calendar.is_active = True
        calendar.save(update_fields=['is_active'])
        queryset = Calendar.objects.filter(therapist=request.user.profile).order_by('week_day')
        context = {'dates': queryset}
        return render(request, 'therapist/partials/partial_calendar_list.html', context)
    context = {
        'calendar': calendar,
        'week_day_name': calendar.get_week_day_display(),
        'schedule_name': calendar.get_schedule_display(),
    }
    return render(request, 'therapist/update_calendar.html', context)
