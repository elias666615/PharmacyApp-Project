from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.db.models.fields import CharField
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name="admin", last_name="admin", phone_number="", country = None, role = None):
        print('*******************' + str(country) + "****************")
        if username is None:
            raise ValueError('Users should have a username')
        if email is None:
            raise ValueError('Users should have a Email')

        _country = None
        _role = None
        if country != None:
            _country = Country.objects.get(code = country)
        if role != None:
            _role = Role.objects.get(code = role)

        user = self.model(username=username, email=self.normalize_email(email), country = _country, role = _role, first_name=first_name, last_name=last_name, phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise ValueError('Password should not be none')
    
        user = self.create_user(username, email, password)
        user = self.model(username=username, email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff  =True
        user.save()
        return user

class Country(models.Model):
    code = CharField(max_length=2, unique=True, blank=False, null=False)
    description = CharField(max_length=30, unique=True, null=False, blank=False)
    phone_code = CharField(max_length=10, unique=True, blank=False, null=False)

    def __str__(self):
        return self.description


class Role(models.Model):
    code = CharField(max_length=3, null=False, unique=True, blank=False)
    description = CharField(max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.description


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=225, unique=True, db_index=True)
    email = models.EmailField(max_length=225, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=False, blank=False, default="first_name")
    last_name = models.CharField(max_length=30, null=False, blank=False, default="last_name")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }



class Card_Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    expiry_pate = models.CharField(max_length=5, null=False, blank=False)
    name_on_card = models.CharField(max_length=30, null=False, blank=False)
    cvv = models.CharField(max_length=3, null=False, blank=False)


class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.TextField(null=False, blank=False)