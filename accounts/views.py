from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, UpdateView, DetailView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, views as auth_views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from treatments.models import Treatment
from .forms import SignUpForm, UserLoginForm, ProfileModelForm, ResetPasswordForm
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
            'Idade': profile.age,
            'Queixas': profile.complaint,
            'Tratamento psiquiátrico': profile.get_psychiatric_display,
            'CRP': profile.crp,
            'Contato de emergência': profile.emergency_number,
            'Plataforma preferida': profile.platform,
            'De acordo com as diretrizes do CRP': profile.get_crp_check_display(),
            'Tem treinamento especializado em emergência': profile.get_trained_display(),
            'Link para termo preenchido de cadastro do e-Psi': profile.e_psi
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
    treatments = Treatment.objects.none()
    if request.user.profile.crp:
        treatments = Treatment.objects.filter(therapist=request.user.profile.id, is_active=True)
    if request.user.profile.age:
        treatments = Treatment.objects.filter(patient=request.user.profile.id, is_active=True)
    context = {
        'treatments': treatments,
    }
    return render(request, 'home.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/home/'


@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, "Sua conta foi deletada com sucesso.")
        return redirect('landing_page')
    return render(request, 'delete_account.html')


class ResetPasswordView(auth_views.PasswordResetView):
    form_class = ResetPasswordForm
    from_email = 'cuidadopsiemrede@gmail.com'
    html_email_template_name = 'email_templates/reset_password_email_template.html'
    email_template_name = "email_templates/reset_password_email_template.html"
    success_url = reverse_lazy("reset-password-done")
    template_name = "password_reset/reset_password_form.html"
    title = ("Recuperar senha")


class ResetPasswordDoneView(auth_views.PasswordResetDoneView):
    template_name = "password_reset/reset_password_done.html"
    title = 'Recuperaçao de senha enviada'


class ResetPasswordConfirmView(auth_views.PasswordResetConfirmView):
    success_url = reverse_lazy("password-reset-complete")
    template_name = "password_reset/reset_password_confirm.html"


class ResetPasswordCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "password_reset/reset_password_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["login_url"] = 'login'
        return context
