from django.urls import path, include
from django.views.generic.base import TemplateView
from . import consumers

websocket_urlpatterns = [
	path('ws/chat/<room_name>/', consumers.ChatConsumer),
]
