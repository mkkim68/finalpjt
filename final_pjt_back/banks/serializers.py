from rest_framework import serializers
from .models import Deposit, DepositOptions, Saving, SavingOptions, Exchange

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'

class DepositOptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ['deposit']

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saving
        fields = '__all__'

class SavingOptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ['saving']

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'