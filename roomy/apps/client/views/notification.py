from django.shortcuts import render
from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from apps.core.roomy_core.models import *

context = {
    "TITLE": "Roomy"
}



class notification(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"Added {self.channel_name} channel to gossip")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} channel to gossip")

    async def user_gossip(self, event):
        await self.send_json(event)
        print(f"Got message {event} at {self.channel_name}")

def demo(request):

    return render(request,"notification_demo.html",context)
