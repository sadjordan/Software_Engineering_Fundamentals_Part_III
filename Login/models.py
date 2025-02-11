from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, userid, password=None, first_name='', last_name=''):
        if not userid:
            raise ValueError('The User ID must be set')
        
        user = self.model(userid=userid, first_name=first_name, last_name=last_name)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, password=None, first_name='', last_name=''):
        user = self.create_user(userid, password, first_name, last_name)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    userid = models.CharField(max_length=200, primary_key=True, null=False)
    password = models.CharField(max_length=128, null=False)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    USERNAME_FIELD = 'userid'
    
    objects = MyUserManager()

    def __str__(self):
        return self.userid
