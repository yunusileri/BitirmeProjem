from django.urls import path, re_path
from .views import *

app_name = 'kullanici'

urlpatterns = [

    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
