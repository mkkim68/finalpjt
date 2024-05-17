from django.db import models
from django.contrib.auth.models import AbstractUser
from banks.models import Deposit, Saving

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    income = models.IntegerField(blank=True, null=True)
    favorite_bank = models.TextField(blank=True, null=True)
    invest_type = models.TextField(blank=True, null=True)
    deposit = models.ManyToManyField(Deposit, blank=True)
    saving = models.ManyToManyField(Saving, blank=True)