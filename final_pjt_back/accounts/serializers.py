from rest_framework import serializers
# from .models import User
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
# User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False)
    balance = serializers.IntegerField(required=False)
    income = serializers.IntegerField(required=False)
    favorite_bank = serializers.CharField(required=False, allow_blank=True, max_length=250)
    invest_type = serializers.CharField(required=False, allow_blank=True, max_length=250)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = self.validated_data.get('username', '')
        data['password1'] = self.validated_data.get('password1', '')
        data['age'] = self.validated_data.get('age', '')
        data['balance'] = self.validated_data.get('balance', '')
        data['income'] = self.validated_data.get('income', '')
        data['favorite_bank'] = self.validated_data.get('favorite_bank', '')
        data['invest_type'] = self.validated_data.get('invest_type', '')
        return data
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields=['deposit', 'saving']

