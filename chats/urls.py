from django.urls import path
from .views import chat

app_name = 'chats'
urlpatterns = [
    path('chat/', chat, name='chat'),
    ]