from django.urls import path

from apps.chat.views import *

app_name = 'chat'

urlpatterns = [
    path('chat/', ChatView.as_view()),
]
