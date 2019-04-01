from django import forms
from .models import *


class ChatCreateForm(forms.ModelForm):
	class Meta:
		model = Chat
		fields = ['title']

class MessageCreateForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['content']

class JoinChatForm(forms.Form):
	title = forms.CharField(max_length=20)
