from django.urls import path
from . import views

urlpatterns = [
    path('deposits/', views.deposit_list)
]
