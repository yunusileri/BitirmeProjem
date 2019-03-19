from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def home_view(request):
    return render(request, 'home.html')


def create_accounts(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(request, username=user.username, password=user.password)
        login(request, new_user)
        return redirect('accounts:home')
    return render(request, 'createForm.html', {'forms': form, 'title': 'Uye Ol'})


def list_accounts(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def LogOut(request):
    logout(request)
    return redirect('accounts:home')


def SignIn(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request,user)
        return redirect('accounts:home')
    return render(request, 'createForm.html', {'forms': form, 'title': 'Giriş Yap'})

