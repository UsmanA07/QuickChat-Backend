from rest_framework import serializers

from apps.user.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'password', 'username', 'phone', 'email')