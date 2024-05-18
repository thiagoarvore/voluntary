from django.urls import path
from django.shortcuts import render
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views


def first_login_view(request):
    return render(request, 'firstlogin.html', {})


urlpatterns = [
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('firstlogin/', first_login_view, name='firstlogin'),
    path('firstlogin/therapist/', views.FirstTherapistView.as_view(), name='firstlogintherapist'),
    path('firstlogin/patient/', views.FirstPatientView.as_view(), name='firstloginpatient'),
    path('profile/<str:pk>', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:pk>/edit', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('home/', views.home_view, name='home'),
    path('about_us/', views.about, name='about_us'),
    path('change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('delete_user/', views.delete_account, name='delete_user'),
]
