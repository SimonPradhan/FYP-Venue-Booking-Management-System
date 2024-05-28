from django.urls import path
from .views import chat
from . import views

app_name = 'chats'
urlpatterns = [
    path('chat/', views.room_view, name='chat'),
    path('chat2/', views.chat, name='chat2'),
    # path('', views.index_view, name='chat-index'),
    # path('<str:room_name>/', views.room_view, name='chat-room'),
    ]