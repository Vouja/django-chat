from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Chat(models.Model):
	title = models.CharField(max_length=20, unique=True)
	users = models.ManyToManyField(User)

	def get_absolute_url(self):
		return reverse('chat', kwargs={'chat_id': self.id})

	def __str__(self):
		return self.title



class Message(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
	class Meta:
		ordering = ['-time']
