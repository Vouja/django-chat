from asgiref.sync import async_to_sync
from .models import *
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
import json

class ChatConsumer(WebsocketConsumer):
	def connect(self):
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
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

		chat_id = text_data_json['chat_id']
		user_id = text_data_json['user_id']
		chat = Chat.objects.get(id=chat_id)
		user = User.objects.get(id=user_id)

		message = text_data_json['message']
		if message == 'reload_messages':
			messages = Message.objects.filter(chat=chat)[:10][::-1]
			for mes in messages:
				self.send(text_data=json.dumps({
					'message': mes.content,
					'username': mes.user.username,
		        }))
		else:
			msg = Message(content=message, user=user, chat=chat)
			msg.save()

        	# Send message to room group
			async_to_sync(self.channel_layer.group_send)(
				self.room_group_name,
            	{
					'type': 'chat_message',
					'message': message,
					'username': user.username,
            	}
        	)

    # Receive message from room group
	def chat_message(self, event):

		message = event['message']
		username = event['username']

        # Send message to WebSocket
		self.send(text_data=json.dumps({
			'message': message,
			'username': username,
        }))
