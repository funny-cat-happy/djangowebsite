from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.core.cache import cache


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'temporary_chat'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        chat_inf = cache.get('ChatInf')
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'UserInf': chat_inf
            }
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        print(bytes_data)
        message_json = json.loads(text_data)
        chat_inf=cache.get('ChatInf')
        if chat_inf is None:
            chat_inf=[]
        chat_inf.append(message_json)
        cache.set('ChatInf',chat_inf,timeout=60*60)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'UserInf': chat_inf
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        user_inf = event['UserInf']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'user_inf': user_inf
        }))