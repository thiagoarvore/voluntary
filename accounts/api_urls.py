from django.urls import path
from . import api_views


urlpatterns = [
    path('accounts/', api_views.AccountListCreateAPIView.as_view(), name='create_list_account'),
    path('acconut/<str:pk>/', api_views.AccountRetrieveUpdateDestroyAPIView.as_view(), name='account_detail'),
    path('accounts/stats/', api_views.AccountStatsView.as_view(), name='account_stats'),
]
