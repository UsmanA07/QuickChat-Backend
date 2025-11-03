from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from apps.chat.serializers import CreateSendSerializer


class CreateSendView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @staticmethod
    def post(request):
        serializer = CreateSendSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        print('\n\n\n')
        print(serializer)
        print(serializer.data)
        print('\n\n\n')
        return Response(status=201)