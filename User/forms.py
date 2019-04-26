import hashlib
from django import forms
from django.contrib.auth import authenticate

from .models import User

"""

"""
class LoginForm(forms.Form):
    tc = forms.CharField(max_length=11, min_length=11)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola')

    def clean(self):
        tc = self.cleaned_data.get('tc')
        tc = hashlib.sha256(tc.encode('utf-8')).hexdigest()
        password = self.cleaned_data.get('password')
        if tc and password:
            user = authenticate(username=tc, password=password)
            if not user:
                raise forms.ValidationError('Kullanıcı Adını veya Paraloyı yanlış girdiniz!')
        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    tc = forms.CharField(max_length=11, min_length=11, label='tc')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Parola Doğrulama')

    class Meta:
        model = User
        fields = [
            'tc',
            'isim',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parolalar Eşleşmiyor')