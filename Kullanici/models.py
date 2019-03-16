from django.db import models


# Create your models here.

class Kullanici:
    kullaniciAdi = models.CharField(max_length=120, verbose_name='Kullanıcı Adı')
    Parola = models.CharField(max_length=64, verbose_name='Parola')
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    eMail = models.EmailField()
