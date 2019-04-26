from django.contrib import admin

from django.contrib import admin

from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['isim']  # Listelerken Göstermek için

    list_display_links = ['isim']  # link oluşturmak için

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
