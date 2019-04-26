import hashlib
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm
from .models import User


def home_view(request):
    users = User.object.all()  # bütün user objeleri çekilir.
    context = {'users': users, 'title': 'Anasayfa'}  # user objeleri html sayfasına parametre olarak gönderilir.
    return render(request, 'home.html', context=context)


def login_view(request):
    """
        login sayfasından alınan kullanıcı adı bilgisi sha-256 ile hashlenerek,
        parola ise djangonun varsayılan olarak kullandığı pkbfdk2(tam ad) algoritmalarını kullanılarak hashlenir ve
        authenticate fonksiyonuna parametre olarak gönderilir ve geçerli kullanıcı varsa kullanıcı grişi sağlanır.
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('tc')
        username = hashlib.sha256(username.encode('utf-8')).hexdigest()
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('users:home')
    return render(request, 'form.html', {'forms': form, 'title': 'Giriş'})


def register_view(request):
    """
        tckimlik numarsası sha-256 ile hashlenerek parola ise djangonun setpassword fonksiyonunu kullanarak
        hashlenerek veritabanına kayıt edilir.
    """
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)

        user.tc = hashlib.sha256(user.tc.encode('utf-8')).hexdigest()
        user.save()

        new_user = authenticate(request, username=user.tc, password=password)
        login(request, new_user)
        return redirect('users:home')

    return render(request, 'form.html', {'forms': form, 'title': 'Kayıt'})


def logout_view(request):
    # çıkış işleminin gerçekleştirildiği komut satırlarıdır.
    logout(request)
    return redirect('users:home')
