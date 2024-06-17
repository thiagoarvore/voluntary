from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


def index(request):
    return render(request, 'landingpage.html', {})

def contract(request):
    return render(request, 'therapist/contract.html', {})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='landing_page'),
    path('contract/', contract, name='contract_page'),
    path('', include('accounts.urls')),
    path('', include('calendars.urls')),
    path('', include('treatments.urls')),
    path('', include('usage_agreement.urls')),
    path('api/v1/', include('accounts.api_urls')),
    path('api/v1/', include('calendars.api_urls')),
    path('api/v1/', include('treatments.api_urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
