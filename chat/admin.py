from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


class ChatAdmin(admin.ModelAdmin):
	list_display = ['title', 'get_users']
	list_filter = ['title']

	def get_users(self, obj):
		return ', \n'.join([user.username for user in obj.users.all()])
	get_users.short_description = 'users'

class MessageAdmin(admin.ModelAdmin):
	list_display = ['chat', 'content', 'user', 'time']
	list_filter = ['time']

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
