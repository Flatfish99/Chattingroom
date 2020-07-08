# chat/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    userlist={}
    logined =[]
    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]
        ChatConsumer.logined.append(str(self.user))
        try:
            ChatConsumer.userlist[self.room_name].append(str(self.user))
        except KeyError:
            dic={str(self.room_name):[]}
            ChatConsumer.userlist.update(dic)
            ChatConsumer.userlist[str(self.room_name)].append(str(self.user))


        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,

        )

        await self.accept()
        message = str(self.user)+' 进入了房间\n'
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name' : '系统通知',
                'time' : 'NOTICE',
                'm_type': 's_message',
                'userlist': ChatConsumer.userlist,
            }
        )
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(

            self.room_group_name,
            self.channel_name
        )
        ChatConsumer.logined.remove(str(self.user))
        ChatConsumer.userlist[str(self.room_name)].remove(str(self.user))
        if(ChatConsumer.userlist[str(self.room_name)]==[]):
            del ChatConsumer.userlist[self.room_name]

        message = str(self.user)+(' 离开了房间\n')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name': "系统通知",
                'time': 'NOTICE',
                'm_type': 's_message',
                'userlist': ChatConsumer.userlist,
            }
        )
    # Receive message from WebSocket

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message =text_data_json['message']
        name = text_data_json['name']
        time = text_data_json['time']
        type = text_data_json['m_type']
        userlist = text_data_json['userlist']


        # Send message to room group

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'name' : name,
                'time' : time,
                'm_type' : type,
                'userlist' : userlist,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        name = event['name']
        time = event['time']
        type = event['m_type']
        userlist = event['userlist']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'name' : name,
            'time': time,
            'm_type' :type,
            'userlist': userlist,
        }))