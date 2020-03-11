
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class booking_notif(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add(self.scope['user'].id, self.channel_name)
        print(
            f'Added {self.channel_name} to self channel {self.scope["user"].id}')
        # self.scope['session']['channel_name'] = self.channel_name
        # self.scope['session'].save()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.scope['user'].id, self.channel_name)

    async def user_message(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")

    async def websocket_received(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })
