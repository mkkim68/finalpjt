from django.urls import path
from . import views

urlpatterns = [
    # path('save-saving-products/', views.save_saving_products),
    path('deposits/', views.deposit_list),
    path('deposit-options/', views.deposit_option_list),
    path('deposits/<str:fin_prdt_cd>/', views.deposit_detail),
    path('savings/', views.saving_list),
    path('saving-options/', views.saving_option_list),
    path('savings/<str:fin_prdt_cd>/', views.saving_detail),
]
