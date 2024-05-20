from django.urls import path
from . import views

urlpatterns = [
    path('deposits/', views.deposit_list),
    path('deposit-options/', views.deposit_option_list),
    path('deposits/<str:fin_prdt_cd>/', views.deposit_detail),
    path('savings/', views.saving_list),
    path('saving-options/', views.saving_option_list),
    path('savings/<str:fin_prdt_cd>/', views.saving_detail),
    path('exchange/', views.exchange),
    path('local/exchange/', views.get_local_exchange, name='get_local_exchange'),
    path('banks/', views.bank_list),
]