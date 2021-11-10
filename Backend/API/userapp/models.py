from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)
        user.save(using=self._db)
        return user

class Country(models.Model):
    code = models.CharField(max_length=4, unique=True)
    country = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.country


class Role(models.Model):
    code = models.CharField(max_length=4, unique=True)
    description = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.description


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length= 250, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    country = models.OneToOneField(Country, on_delete=models.SET_NULL, null=True)
    role = models.OneToOneField(Role, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length= 30, null=False, unique=False, blank=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Card_Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    card_number = models.CharField(max_length=16, null=False, blank=False)
    expiry_pate = models.CharField(max_length=5, null=False, blank=False)
    name_on_card = models.CharField(max_length=30, null=False, blank=False)
    cvv_number = models.CharField(max_length=3, null=False, blank=False)


class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    location = models.TextField(null=False, blank=False)
