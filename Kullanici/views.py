from django.shortcuts import render


# Create your views here.

def kullanici_home_view(request):
    return render(request, 'home.html')
