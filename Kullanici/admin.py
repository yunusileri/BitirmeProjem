from django.contrib import admin
from .models import KullaniciModel


# Register your models here.
class KullaniciAdmin(admin.ModelAdmin):
    list_display = ['kullaniciAdi', 'Parola']

    class Meta:
        model = KullaniciModel


admin.site.register(KullaniciModel, KullaniciAdmin)

