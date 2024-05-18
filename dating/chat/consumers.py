from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import sync_to_async
import json
from .models import ChatGroup, GroupMessage, User

class ChatroomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.chatroom_name = self.scope['url_route']['kwargs']['group_name']
        self.chatroom = await sync_to_async(get_object_or_404)(ChatGroup, group_name=self.chatroom_name)

        await self.channel_layer.group_add(
            self.chatroom_name, self.channel_name
        )

        users_online = await sync_to_async(list)(self.chatroom.users_online.all())
        if self.user not in users_online:
            await sync_to_async(self.chatroom.users_online.add)(self.user)
            await self.update_online_count()

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.chatroom_name, self.channel_name
        )
        users_online = await sync_to_async(list)(self.chatroom.users_online.all())
        if self.user in users_online:
            await sync_to_async(self.chatroom.users_online.remove)(self.user)
            await self.update_online_count()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']

        message = await sync_to_async(GroupMessage.objects.create)(
            body=body,
            author=self.user,
            group=self.chatroom
        )
        event = {
            'type': 'message_handler',
            'message_id': message.id,
        }
        await self.channel_layer.group_send(
            self.chatroom_name, event
        )

    async def message_handler(self, event):
        message_id = event['message_id']
        message = await sync_to_async(GroupMessage.objects.get)(id=message_id)
        context = {
            'message': message,
            'user': self.user,
            'chat_group': self.chatroom
        }
        html = await sync_to_async(render_to_string)("chat/partials/chat_message_p.html", context=context)
        await self.send(text_data=json.dumps({'html': html}))

    async def update_online_count(self):
        online_count = await sync_to_async(self.chatroom.users_online.count)() - 1
        event = {
            'type': 'online_count_handler',
            'online_count': online_count
        }
        await self.channel_layer.group_send(self.chatroom_name, event)

    async def online_count_handler(self, event):
        online_count = event['online_count']

        # Fetch chat messages asynchronously
        chat_messages = await sync_to_async(list)(self.chatroom.chat_messages.all())
        chat_messages = chat_messages[:30]  # Subscripting after retrieving chat messages

        # Fetch author IDs asynchronously
        author_ids = set()
        for message in chat_messages:
            author_ids.add(await sync_to_async(lambda: message.author.id)())

        # Fetch users asynchronously
        users = User.objects.filter(id__in=author_ids).all()

        context = {
            'online_count': online_count,
            'chat_group': self.chatroom,
            'users': users
        }
        html = await sync_to_async(render_to_string)("chat/partials/online_count.html", context)
        await self.send(text_data=json.dumps({'html': html}))

