from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View
from .models import *
from .forms import *
from django.http import HttpResponse
from django.db.models.functions import *
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
import json


class HomeView(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return render(request, 'chat/home.html')
		user = request.user
		join_form = JoinChatForm()
		chat_list = Chat.objects.filter(users=user)
		return render(request, 'chat/home.html', context={
			'chat_list': chat_list,
			'join_form': join_form,
		})
	def post(self, request):
		if not request.user.is_authenticated:
			return render(request, 'chat/home.html')
		user = request.user
		join_form = JoinChatForm(request.POST)
		if join_form.is_valid():
			title = join_form.cleaned_data.get('title')
			try:
				chat = Chat.objects.get(title=title)
			except:
				chat = None
			if chat:
				chat.users.add(user)
		chat_list = Chat.objects.filter(users=user)
		return render(request, 'chat/home.html', context={
			'chat_list': chat_list,
			'join_form': join_form,
		})

class ChatCreate(View):
	def get(self, request):
		if not request.user.is_authenticated:
			return render(request, 'chat/home.html')
		new_chat_form = ChatCreateForm()
		return render(request, 'chat/chat_create.html', context={
			'form': new_chat_form,
		})
	def post(self, request):
		if not request.user.is_authenticated:
			return render(request, 'chat/home.html')
		new_chat_form = ChatCreateForm(request.POST)

		if new_chat_form.is_valid():
			chat = new_chat_form.save()
			user = request.user
			chat.users.add(user)
		return redirect(reverse('home'))

class ChatEngine(View):
	def get(self, request, chat_id):
		if not request.user.is_authenticated or not get_object_or_404(Chat.objects.filter(id=chat_id), users=request.user):
			return render(request, 'chat/home.html')
		return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(chat_id)),
		'user': request.user.id,
		'chat': chat_id,
    })
