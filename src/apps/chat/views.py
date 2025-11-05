from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from apps.chat.serializers import CreateChatSerializer


class CreateChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = CreateChatSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        return Response(status=201)
