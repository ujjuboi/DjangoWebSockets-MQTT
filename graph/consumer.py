from channels.generic.websocket import AsyncWebsocketConsumer
import json

class Graph(AsyncWebsocketConsumer):

    #connect
    async def connect(self):
        self.groupname = "Dashboard"
        await self.channel_layer.group_add(
            #add groupname first the channel_name
            self.groupname,
            self.channel_name,
        )
        await self.accept()

    #disconnect
    async def disconnect(self, close_code):
        pass

    #recieve
    async def receive(self, text_data):

        data        = json.loads(text_data)
        actualValue = data['value']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'senddata',
                'value': actualValue,
            }
        )
        print('You are in graph page', text_data)

    #send data based on recieve group_send()
    async def senddata(self, event):
        sendvalue = event['value']
        await self.send(json.dumps({'value': sendvalue}))