from django.urls import path
from django.shortcuts import render


def usage_agreement(request):
    return render(request, 'usage_agreement.html', {})


def privacy_policy(request):
    return render(request, 'privacy_policy.html', {})


urlpatterns = [
    path('usage_agreement/', usage_agreement, name='usage_agreement'),
    path('privacy_policy/', privacy_policy, name='privacy_policy')
]
