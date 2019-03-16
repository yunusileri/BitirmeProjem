from django.urls import path, re_path
from .views import *

app_name = 'kullanici'

urlpatterns = [
    path('', kullanici_home_view, name='home'),
    path('index/', kullanici_index, name='index'),
    path('create/', kullanici_create, name='create'),

]
