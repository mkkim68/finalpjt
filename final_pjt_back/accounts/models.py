from django.db import models
from django.contrib.auth.models import AbstractUser
from banks.models import Deposit, Saving

# Create your models here.
class User(AbstractUser):
    deposit = models.ManyToManyField(Deposit, blank=True)
    saving = models.ManyToManyField(Saving, blank=True)