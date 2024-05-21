from django.urls import path
from . import views

urlpatterns = [
    #예금
    path('deposits/', views.deposit_list),
    path('deposit-options/', views.deposit_option_list),
    path('deposits/<str:fin_prdt_cd>/', views.deposit_detail),
    path('deposits/<str:fin_prdt_cd>/', views.deposit_detail),
    path('deposits/<str:fin_prdt_cd>/option/', views.deposit_detail_option),
    path('deposits/<str:fin_prdt_cd>/join/', views.deposit_detail_join),
    #적금
    path('savings/', views.saving_list),
    path('saving-options/', views.saving_option_list),
    path('savings/<str:fin_prdt_cd>/', views.saving_detail),
    path('savings/<str:fin_prdt_cd>/option/', views.saving_detail_option),
    #환율
    path('exchange/', views.exchange),
    path('local/exchange/', views.get_local_exchange, name='get_local_exchange'),
    #지도
    path('banks/', views.bank_list),
]