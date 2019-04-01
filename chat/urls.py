from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import TemplateView
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('create/', ChatCreate.as_view(), name='chat_create'),
	path('chat/<int:chat_id>/', ChatEngine.as_view(), name='chat'),
	path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
