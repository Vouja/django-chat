from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from chat.views import HomeView


urlpatterns = [
	path('', loginu, name='login'),
	path('register/', signup, name='register'),
]
