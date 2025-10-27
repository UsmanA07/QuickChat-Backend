from rest_framework import generics
from rest_framework import viewsets
from apps.user.models import User
from apps.user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self):
        return User.objects.create_user()

