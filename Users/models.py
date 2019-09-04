from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
import jwt
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse


class UserManager(BaseUserManager):
 
    def create_user(self, email, first_name, last_name, password=None):
        
        if email is None:
            raise TypeError('The given email must be set') 
        if first_name is None:
            raise TypeError('First name is requiered')
        if last_name is None:
            raise TypeError('Last name is requiered')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(
            email, 
            first_name=first_name, 
            last_name=last_name, 
            ) 
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):       
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    

