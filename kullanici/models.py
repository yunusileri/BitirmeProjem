from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import hashlib


class UserManager(BaseUserManager):
    def create_user(self, tc, name, password=None, is_active=True, is_staff=False, is_admin=False):  # ,name
        if not tc:
            raise ValueError('Gecerli bir email adresi giriniz!')
        if not password:
            raise ValueError('Gecerli bir parola adresi giriniz!')
        user_obj = self.model(
            tc=hashlib.sha256(tc.encode('utf-8')).hexdigest()

        )
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.set_password(password)
        user_obj.name = name
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, tc, password=None):
        user = self.create_user(
            tc,
            password=password,
            is_staff=True
        )
        return user

    def create_superuser(self, tc, password=None, name=None):
        user = self.create_user(
            tc,
            name=name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    tc = models.CharField(max_length=128, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=True)  # staff user non superuser
    admin = models.BooleanField(default=True)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'tc'  # username
    REQUIRED_FIELDS = ['name']  # ['name']
    object = UserManager()

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

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
