from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_active, is_staff, is_superuser, **extra_fields):
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

class Role(models.Model):
    code = models.CharField(max_length=4, unique=True)
    country = models.CharField(max_length=30, unique=True)

class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length= 250, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    phone_number = PhoneNumberField()

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []