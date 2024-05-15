from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.utils.translation import gettext_lazy as _
from .models import Profile


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("As senhas não coincidem.")
        self.error_messages['duplicate_username'] = _("Este nome de usuário já está em uso.")
        self.error_messages['invalid_username'] = _("O nome de usuário deve conter apenas letras, números e @/./+/-/_ caracteres.")
        self.error_messages['password_too_short'] = _("A senha é muito curta.")
        self.error_messages['password_too_common'] = _("Esta senha é muito comum.")
        self.error_messages['password_entirely_numeric'] = _("A senha não pode ser completamente numérica.")
        self.help_texts = {
            'username': _('Este será seu nome de usuário único, e será apenas utilizado para login.'),
            'password1': _(''),
            'password2': _('Digite a mesma senha novamente para verificação.'),
        }


class ProfileModelForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'photo', 'address', 'name', 'whatsapp', 'uf',
            'city', 'age', 'complaint', 'psychiatric',
            'emergency_number', 'crp', 'crp_check', 'platform', 'trained',
        ]
        widgets = {
            'city': forms.Select(attrs={}),
            'uf': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)


class UserLoginForm(AuthenticationForm):
    pass


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("As senhas não coincidem.")
        self.error_messages['password_too_common'] = _("Esta senha é muito comum.")
        self.error_messages['password_entirely_numeric'] = _("A senha não pode ser completamente numérica.")
