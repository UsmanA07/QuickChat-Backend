from rest_framework import serializers

from apps.user.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']