from django.contrib import admin

from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['name']  # Listelerken Göstermek için

    list_display_links = ['name']  # link oluşturmak için

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
