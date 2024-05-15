from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from treatments.models import Treatment
from .forms import SignUpForm, UserLoginForm, ProfileModelForm
from .models import Profile


def about(request):
    profiles = Profile.objects.all()
    context = {}
    context['profiles'] = profiles
    return render(request, 'about_us.html', context)


class SignUpView(FormView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = '/firstlogin/'  # Redireciona para a página firstlogin após o cadastro

    def form_valid(self, form):
        form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'login.html'
    success_url = '/home/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if not user.profile.city:
                return redirect('firstlogin')
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


@method_decorator(login_required(login_url='login'), name='dispatch')
class FirstTherapistView(UpdateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'therapist/first.html'
    success_url = '/home/'

    def get_object(self, queryset=None):
        return self.request.user.profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class FirstPatientView(UpdateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'patient/first.html'
    success_url = '/home/'

    def get_object(self, queryset=None):
        return self.request.user.profile


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_object(self):
        user = self.request.user
        return user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        fields = {
            'Endereço': profile.address,
            'Telefone Celular': profile.whatsapp,
            'Cidade': profile.city,
            'UF': profile.uf,
            'age': profile.age,
            'complaint': profile.complaint,
            'psychiatric': profile.psychiatric,
            'CRP': profile.crp,
            'emergency_number': profile.emergency_number,
            'Plataforma preferida': profile.platform,
            'De acordo com as diretrizes do CRP': profile.crp_check,
            'Tem treinamento especializado em emergência': profile.trained
        }
        context['fields'] = fields
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileModelForm
    template_name = 'edit_profile.html'
    success_url = '/profile/'

    def get_object(self):
        user = self.request.user
        return user.profile

    def get_success_url(self):
        return reverse_lazy(
            'profile',
            kwargs={'pk': self.object.pk}
        )


@login_required(login_url='login')
def home_view(request):
    if request.user.profile.crp:
        treatments = Treatment.objects.filter(therapist=request.user.profile, is_active=True)
    if request.user.profile.age:
        treatments = Treatment.objects.filter(patient=request.user.profile, is_active=True)
    return render(request, 'home.html', {'treatments': treatments})


@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/home/'


@method_decorator(login_required(login_url='login'), name='dispatch')
class ResetPasswordView(auth_views.PasswordResetView):
    success_url = '/home/'
