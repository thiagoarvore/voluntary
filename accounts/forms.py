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
        self.fields['username'].label = 'Nome de usuário'
        self.fields['email'].label = 'Endereço de e-mail'
        self.fields['password1'].label = 'Senha'
        self.fields['password2'].label = 'Confirmação de senha'
        self.fields['username'].error_messages.update({
            'required': _("Este campo é obrigatório."),
            'unique': _("Este nome de usuário já está em uso."),
            'invalid': _("O nome de usuário não deve conter espaços, deve conter apenas letras, números e @/./+/-/_ caracteres."),
        })
        self.fields['email'].error_messages.update({
            'required': _("Este campo é obrigatório."),
            'invalid': _("Insira um endereço de e-mail válido."),
        })
        self.fields['password1'].error_messages.update({
            'required': _("Este campo é obrigatório."),
            'password_too_short': _("A senha é muito curta."),
            'password_too_common': _("Esta senha é muito comum."),
            'password_entirely_numeric': _("A senha não pode ser completamente numérica."),
        })
        self.fields['password2'].error_messages.update({
            'required': _("Este campo é obrigatório."),
            'password_mismatch': _("As senhas não coincidem."),
        })
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
            'city', 'age', 'complaint', 'psychiatric', 'e_psi',
            'emergency_number', 'crp', 'crp_check', 'platform', 'trained',
        ]
        widgets = {
            'city': forms.Select(),
            'uf': forms.Select(),
        }
        labels = {
            'address': 'Endereço',
            'name': 'Nome',
            'uf': 'Estado',
            'city': 'Cidade',
            'age': 'Idade',
            'complaint': 'Queixas',
            'psychiatric': 'Acompanhamento psiquiátrico',
            'e_psi': 'Link para termo preenchido de cadastro do e-Psi',
            'emergency_number': 'Contato para emergências',
            'crp': 'CRP',
            'platform': 'Plataforma preferida',
            'crp_check': 'Está de acordo com as diretrizes do CRP',
            'trained': 'Possui treinamento de atendimento de emergência',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nome de usuário'
        self.fields['password'].label = 'Senha'


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages['password_mismatch'] = _("As senhas não coincidem.")
        self.error_messages['password_too_common'] = _("Esta senha é muito comum.")
        self.error_messages['password_entirely_numeric'] = _("A senha não pode ser completamente numérica.")
