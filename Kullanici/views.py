from django.contrib import messages
from django.shortcuts import render
from .models import KullaniciModel
from .KullaniciForms import kullaniciForm
from hashlib import sha256


# Create your views here.

def kullanici_home_view(request):
    return render(request, 'home.html')


def kullanici_index(request):
    kullanicilar = KullaniciModel.objects.all()
    return render(request, 'Kullanici/index.html', {'kullanicilar': kullanicilar})


def kullanici_create(request):
    Form = kullaniciForm(request.POST or None)
    if Form.is_valid():
        user = Form.save(commit=False)
        user.Parola = encrypt_string(user.Parola)
        user.save()

        # password2 = Form.cleaned_data.get('Parola2')
        # if password1 and password2 and password1 != password2:
        # messages.error(request, 'Parolalar Eşleşmiyor', extra_tags='mesaj-basarisiz')

        messages.success(request, 'Başarılı Bir Şekilde Oluşturdunuz.', extra_tags='mesaj-basarili')

    context = {'forms': kullaniciForm, 'title': 'Ekle'}
    return render(request, 'Kullanici/createForm.html', context)


def encrypt_string(hash_string):
    sha_signature = \
        sha256(hash_string.encode()).hexdigest()
    return sha_signature
