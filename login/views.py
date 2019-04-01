from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def signup(request):
	if request.user.is_authenticated:
		return redirect('/home')
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/home')
	else:
		form = UserCreationForm()
	return render(request, 'login/signup.html', context={
		'form': form,
	})

def loginu(request):
	if request.user.is_authenticated:
		return redirect('/home')
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/home')
	else:
		form = AuthenticationForm()
	return render(request, 'login/login.html', context={
		'form': form,
	})
