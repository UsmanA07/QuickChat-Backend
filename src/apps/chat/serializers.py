from rest_framework import serializers


class CreateSendSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'