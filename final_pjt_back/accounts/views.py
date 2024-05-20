from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['GET'])
def get_user_by_id(request, user_id):
    if request.method == "GET":
        user = User.objects.get(pk=user_id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

@api_view(['GET']) 
def get_user_by_username(request, username):
    if request.method == "GET":
        user = User.objects.get(username=username)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)