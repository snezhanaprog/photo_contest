import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from datetime import datetime
from urllib.parse import parse_qs


def notify_user(user, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"user_{user.id}",
        {
           "type": "send_notification",
           "notification": {
               "message": message,
               "timestamp": str(datetime.now()),
            },
        }
    )


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        from rest_framework.authtoken.models import Token
        query_string = self.scope['query_string'].decode('utf-8')
        params = parse_qs(query_string)
        key = params.get('token', [None])[0]
        if key:
            token = await Token.objects.select_related('user').aget(key=key)
            self.user = token.user
        else:
            await self.close()
        self.group_name = f"user_{self.user.id}"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_notification(self, event):
        notification = event['notification']
        await self.send(text_data=json.dumps(notification))
