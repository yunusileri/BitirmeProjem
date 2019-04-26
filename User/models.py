from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import hashlib

"""
  UserManager classında ise User clasında oluşturduğumuz özelliklerin
  nasıl saklanacağını ve nasıl kayıt edileceğini oluştururuz.
"""


class UserManager(BaseUserManager):
    def create_user(self, tc, isim, password=None, is_active=True, is_staff=False, is_admin=False):
        if not tc:
            raise ValueError('Geçerli bir TC kimlik numarası giriniz!')
        if not password:
            raise ValueError('Geçerli bir parola adresi giriniz!')
        user_obj = self.model(
            #   Python hashlib modülünü kullanarak tc kimlik numarasını sha256 ile hashleyerek veritabanında saklarız
            tc=hashlib.sha256(tc.encode('utf-8')).hexdigest()

        )
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.isim = isim
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, tc, password=None):
        user = self.create_user(
            tc,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, tc, password=None, isim=None):
        user = self.create_user(
            tc,
            isim=isim,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


"""
   User classı bizim kullanıcı modelimizi oluşturduğumuz kısımdır.
    Tc, isim, parola gibi özellikleri burada oluştururuz.
"""


class User(AbstractBaseUser):
    isim = models.CharField(max_length=255, blank=True, null=True)
    tc = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=True)  # staff user non superuser
    admin = models.BooleanField(default=True)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'tc'  # username
    REQUIRED_FIELDS = ['isim']
    object = UserManager()

    def __str__(self):
        return self.isim

    def get_isim(self):
        return self.isim

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active