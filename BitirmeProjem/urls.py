from django.contrib import admin
from django.urls import path
from django.urls import  include
"""
    django da her app in kendi içinde url tanımlaması yapulabilir. Bu url yönetimini kolaylaştırır.
    İnclude metodu ile User/urls.py dosyası import edilir. 
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls'))
]
