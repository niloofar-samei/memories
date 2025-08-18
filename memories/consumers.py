from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = "chat_room"
        print(f"🔌 CONNECT: {self.channel_name} joined {self.room_group_name}")
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print(f"❌ DISCONNECT: {self.channel_name} left {self.room_group_name}")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def new_photo_message(self, text_data):
        print(f"📥 RECEIVE raw: {text_data}")
        dada = json.loads(text_data)
        message = data["message"]
        print(f"📢 BROADCAST: {message} to {self.room_group_name}")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        print(f"📨 CHAT_MESSAGE handler fired: {event}")
        message = event["message"]

        await self.send(text_data=json.dumps({"type": "chat", "message": message}))
        print(f"✅ SENT to client {self.channel_name}: {message}")
