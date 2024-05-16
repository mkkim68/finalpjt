from rest_framework import serializers
from .models import Deposit, Saving

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'