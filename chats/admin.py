from django.contrib import admin

from chats.models import Room, Message

admin.site.register(Room)
admin.site.register(Message)