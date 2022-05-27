import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ClientConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.client_name = self.scope['url_route']['kwargs']['client_name']

        await self.channel_layer.group_add(
            self.client_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.client_name,
            self.channel_name
        )

    # Receive payload from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        payload = text_data_json['payload']

        # Send payload to client group
        await self.channel_layer.group_send(
            self.client_name,
            {
                'type': 'client_payload',
                'payload': payload
            }
        )

    # Receive payload from client group
    async def client_payload(self, event):
        payload = event['payload']

        # Send payload to WebSocket
        await self.send(text_data=json.dumps({
            'payload': payload
        }))