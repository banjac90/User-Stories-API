from django.db import models
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

    #resset password
@receiver(reset_password_token_created)   
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    #send an email
    context ={
        'crurrent_user': reset_password_token.user,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    }
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_palintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        #title:
        "Password Reset for {title}".format(title="User Stories password reset request"),
        #message:
        email_palintext_message,
        #from:
        "noreplay@somehost.local",
        #to:
        [reset_password_token.user.email]
        )
    msg.attach_alternative(email_html_message,"text/html")
    msg.send()


