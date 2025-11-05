from rest_framework import serializers


class CreateChatSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'