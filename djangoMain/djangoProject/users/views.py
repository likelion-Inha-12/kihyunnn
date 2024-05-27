from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.serializers import UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    email = request.data.get('email')
    userId = request.data.get('userId')
    password = request.data.get('password')
    name = request.data.get('name')
    generation = request.data.get('generation')
    gender = request.data.get('gender')

    serializer = UserSerializer(data=request.data)
    serializer.email = email
    serializer.name = name

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    userId = request.data.get('userId') # id로 로그인으로 수정
    password = request.data.get('password')

    user = authenticate(userId = userId, password=password)
    if user is None:
        return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

    refresh = RefreshToken.for_user(user)
    update_last_login(None, user)

    return Response({'refresh_token': str(refresh),
                     'access_token': str(refresh.access_token), }, status=status.HTTP_200_OK)