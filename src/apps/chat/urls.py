from django.urls import path

from apps.chat.views import *

app_name = 'chat'

urlpatterns = [
    path('send/', CreateSendView.as_view()),
]
