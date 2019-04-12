import hashlib

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from kullanici.forms import LoginForm, RegisterForm
from .models import User


def home_view(request):
    users = User.object.all()
    context = {'users': users, 'title': 'Anasayfa'}
    return render(request, 'home.html', context=context)


def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        # username = request.POST['user_name']
        username = form.cleaned_data.get('tc')

        username = hashlib.sha256(username.encode('utf-8')).hexdigest()
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        login(request, user)
        return redirect('kullanici:home')

    return render(request, 'form.html', {'forms': form, 'title': 'Giriş'})


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = user.tc
        password = form.cleaned_data.get('password1')
        user.set_password(password)

        user.tc = hashlib.sha256(user.tc.encode('utf-8')).hexdigest()

        user.staff = True
        user.admin = True

        user.save()

        new_user = authenticate(request, username=user.tc, password=password)
        login(request, new_user)
        return redirect('kullanici:home')

    return render(request, 'form.html', {'forms': form, 'title': 'Kayıt'})


def logout_view(request):
    logout(request)
    return redirect('kullanici:home')
