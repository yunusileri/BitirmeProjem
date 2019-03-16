from django.shortcuts import render
from .models import KullaniciModel


# Create your views here.

def kullanici_home_view(request):
    return render(request, 'home.html')


def kullanici_index(request):
    kullanicilar = KullaniciModel.objects.all()
    return render(request, 'Kullanici/index.html', {'kullanicilar': kullanicilar})
