from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from django.conf import settings
import json
import requests

from apps.chat.serializers import CreateChatSerializer


class CreateChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = CreateChatSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        api_key = settings.API_KEY
        print(request.data)
        print('\n\n\n\n\n')
        data = json.dumps({
            'channel': f'user:{request.data['recipient']}',
            'data': request.data
        })
        headers = {'Content-type': 'application/json', 'X-API-Key': api_key}
        resp = requests.post('http://127.0.0.1:8001/api/publish', data=data, headers=headers)
        print(resp.json())

        return Response(status=201)


class ChatView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = CreateChatSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        api_key = settings.API_KEY
        print(request.data)
        print('\n\n\n\n\n')
        sort_username = '_'.join(sorted([request.data['recipient'], request.data['sender']]))
        print(sort_username, 'qqqqqqqqq')
        data = json.dumps({
            'channel': f'chat:{sort_username}',
            'data': request.data
        })
        headers = {'Content-type': 'application/json', 'X-API-Key': api_key}
        resp = requests.post('http://127.0.0.1:8001/api/publish', data=data, headers=headers)
        # print(resp.json())

        return Response(status=201)
