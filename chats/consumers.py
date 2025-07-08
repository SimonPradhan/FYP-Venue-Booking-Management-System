import json
from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from .models import Room, Message
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    # @database_sync_to_async
    # def get_room(self):
    #     try:
    #         return Room.objects.get(name=self.room_name)
    #     except Room.DoesNotExist:
    #         return None
        
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.room = Room.objects.get(name=self.room_name)
        print(self.room)
        # self.room = await self.get_room()
        self.user = self.scope['user']
        self.user_inbox = f'{self.user.username}_inbox'
    

        # # Determine if the user is a vendor or a regular user
        # if self.user == self.room.user_id:
        #     self.vendor = self.room.vendor_id
        # elif self.user == self.room.vendor_id:
        #     self.vendor = self.room.user_id

        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        # Join the user inbox group
        self.channel_layer.group_add(
            self.user_inbox,
            self.channel_name,
        )

        # Send the user list to the newly joined user
        self.send_user_list()

        # Notify other users about the user join event
        self.send_user_join_message()

        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if not self.user.is_authenticated:
            return
        else:
            self.send(text_data=json.dumps({
                'type': 'chat_message',  # Add a 'type' field here
                'message': message,
                'user': self.user.username,
            }))

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                # 'user': self.user.username,
                'message': message,
            }
        )
        Message.objects.create(user=self.user, room=self.room, content=message)

        
    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        self.room.leave(self.user)
        self.channel_layer.group_discard(
            self.user_inbox,
            self.channel_name,
        )

        # Notify other users about the user leave event
        self.send_user_leave_message()
    

        

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(event))

    async def private_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def private_message_delivered(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_user_list(self):
        active_users = [user.username for user in self.room.online.all()]
        await self.send(text_data=json.dumps({
            'type': 'user_list',
            'users': active_users,
        }))

    async def send_user_join_message(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_join',
                'user': self.user.username,
            }
        )

    async def send_user_leave_message(self):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'user_leave',
                'user': self.user.username,
            }
        )

    async def user_join(self, event):
        # Handle the user join event
        pass  # You can implement the logic here if needed

    async def user_leave(self, event):
        # Handle the user leave event
        pass  # You can implement the logic here if needed


