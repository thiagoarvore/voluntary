from django.urls import path
from django.shortcuts import render
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
    path('delete_user/', views.delete_account, name='delete_user'),
    path('reset_password/', views.ResetPasswordView.as_view(), name='password-reset'),
    path('reset_password_done', views.ResetPasswordDoneView.as_view(), name='reset-password-done'),
    path('reset_password/confirm/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='password-reset-confirm'),
    path('reset_password/complete/', views.ResetPasswordCompleteView.as_view(), name='password-reset-complete'),
]
