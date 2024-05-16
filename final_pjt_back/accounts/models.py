from django.db import models
from django.contrib.auth.models import AbstractUser
from banks.models import Deposit, Saving

# Create your models here.
class User(AbstractUser):
    age = models.IntegerField(blank=True)
    balance = models.IntegerField(blank=True)
    income = models.IntegerField(blank=True)
    favorite_bank = models.TextField()
    invest_type = models.TextField()
    deposit = models.ManyToManyField(Deposit, blank=True)
    saving = models.ManyToManyField(Saving, blank=True)