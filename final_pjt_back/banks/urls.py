from django.urls import path
from . import views

urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('save-saving-products/', views.save_saving_products),
    path('deposits/', views.deposit_list),
    path('deposits/<str:fin_prdt_cd>/', views.deposit_detail),
    path('savings/', views.saving_list),
    path('savings/<str:fin_prdt_cd>/', views.saving_detail),
]
