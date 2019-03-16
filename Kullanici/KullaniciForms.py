from django import forms
from .models import KullaniciModel
from django.contrib import messages


class kullaniciForm(forms.ModelForm):
    Parola2 = forms.CharField(max_length=120, widget=forms.PasswordInput, label='Parola2')

    class Meta:
        model = KullaniciModel
        fields = [
            'kullaniciAdi',
            'Parola',
            'Parola2',
            'isim',
            'soyisim',
            'eMail',
        ]

    # def clean_Parola2(self):
    #     password1 = self.cleaned_data.get('Parola')
    #     password2 = self.cleaned_data.get('Parola2')
    #     if password1 and password2 and password1 != password2:
    #         raise messages.error(self, 'hataaaaa')
