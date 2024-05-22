from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from banks.models import Deposit, DepositOptions, Saving, SavingOptions
from .models import User
from banks.serializers import DepositSerializer, DepositOptionsSerializers, SavingSerializer, SavingOptionsSerializers
from .serializers import CustomUserSerializer

User = get_user_model()

# @api_view(['GET'])
# def get_user_by_id(request, user_id):
#     if request.method == "GET":
#         user = User.objects.get(pk=user_id)
#         serializer = CustomUserSerializer(user)
#         return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_by_id(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    deposits = user.deposit_set.all()
    savings = user.saving_set.all()
    
    deposit_data = []
    for deposit in deposits:
        options = DepositOptions.objects.filter(deposit=deposit)
        deposit_data.append({
            "deposit": DepositSerializer(deposit).data,
            "options": DepositOptionsSerializers(options, many=True).data
        })
    
    saving_data = []
    for saving in savings:
        options = SavingOptions.objects.filter(saving=saving)
        saving_data.append({
            "saving": SavingSerializer(saving).data,
            "options": SavingOptionsSerializers(options, many=True).data
        })

    data = {
        "user": CustomUserSerializer(user).data,
        "deposits": deposit_data,
        "savings": saving_data
    }

    return Response(data)

@api_view(['GET']) 
def get_user_by_username(request, username):
    if request.method == "GET":
        user = User.objects.get(username=username)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_update(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'PUT' and user == request.user:
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)