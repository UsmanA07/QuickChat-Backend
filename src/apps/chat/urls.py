from django.urls import path

from apps.chat.views import *

app_name = 'chat'

urlpatterns = [
    path('send/', CreateChatView.as_view()),
    path('chat/', ChatView.as_view()),
]
