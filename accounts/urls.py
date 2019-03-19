from django.urls import path, re_path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # path('login/', login_view, name='login'),
    # path('register/', register_view, name='register'),
    # path('logout/', logout_view, name='logout'),
    path('',home_view, name='home'),
    path('create', create_accounts, name='create'),
    path('index', list_accounts, name='index'),
    path('login', SignIn, name='login'),
    path('logout', LogOut, name='logout'),

]