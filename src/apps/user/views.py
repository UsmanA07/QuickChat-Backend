from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.user.dtos import UserRegisterDTO
from apps.user.models import User
from apps.user.serializers import *


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request):
        serializer = CreateUserSerializer(data=request.data)
        print(serializer)
        if not serializer.is_valid():
            print(f'not validated')
            return Response(serializer.errors, status=400)
        user_dto = UserRegisterDTO(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )
        print(user_dto)
        print('\n\n\n\n')
        user = User.objects.create_user(user_dto.username, user_dto.email, user_dto.password)
        print(user)
        return Response(status=201)


class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
