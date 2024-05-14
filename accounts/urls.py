from django.urls import path
from django.shortcuts import render
from .views import SignUpView, LoginView, LogoutView, FirstTherapistView, FirstPatientView, ProfileView, ProfileUpdateView, home_view

def first_login_view(request):
    return render(request, 'firstlogin.html', {})

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('firstlogin/', first_login_view, name='firstlogin'),
    path('firstlogin/therapist/', FirstTherapistView.as_view(), name='firstlogintherapist'),
    path('firstlogin/patient/', FirstPatientView.as_view(), name='firstloginpatient'),
    path('profile/<str:pk>', ProfileView.as_view(), name='profile'),
    path('profile/<str:pk>/edit', ProfileUpdateView.as_view(), name='edit_profile'),
    path('home/', home_view, name='home')
]