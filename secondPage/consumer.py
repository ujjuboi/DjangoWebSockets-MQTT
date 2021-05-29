# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from cryptography.fernet import Fernet
from firstpage.models import UserGroup

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        auth_token = self.scope['url_route']['kwargs']['auth_token']
        if(self.authCheck(auth_token)):
            # Join room group
            self.room_group_name = 'data_%s' % self.room_name
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def authCheck(self, auth_token):
        if(auth_token):
            token = self.decryptToken(auth_token)
            secret = token.get('secret')
            user = UserGroup.objects.get(group = secret).user
            if(user and user.email == token.get('email')):
                return True
            else:
                return False
        else:
            return False

    def decryptToken(self, auth_token):
        file = open('filekey.key', 'rb')
        key = file.read()
        file.close()
        fernet = Fernet(key)
        decrypt = fernet.decrypt(bytes(auth_token,'utf-8'))
        return json.loads(decrypt.decode('utf-8'))