from django.db import models

# Create your models here.
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from django.db.models.fields import CharField
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name="admin", last_name="admin", phone_number="", role = None, **extra_fields):
        print('email: ' + email)
        print('password: ', password)
        if email is None:
            raise ValueError('Users should have a Email')

        _role = None
        if role != None:
            _role = Role.objects.get(code = role)

        user = self.model(email=self.normalize_email(email), role = _role, first_name=first_name, last_name=last_name, phone_number=phone_number)
        print(password)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        print('email: ' + email)
        print('password: ', password)
        if password is None:
            raise ValueError('Password should not be none')
    
        user = self.create_user(email, password, **extra_fields)
        print('user created')
        # user = self.model(username=username, email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff  =True
        user.save()
        return user


class Role(models.Model):
    code = CharField(max_length=3, null=False, unique=True, blank=False)
    description = CharField(max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        return self.description


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=225, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30, null=False, blank=False, default="first_name")
    last_name = models.CharField(max_length=30, null=False, blank=False, default="last_name")
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=50, null=True, blank=False)
    street = models.CharField(max_length=50, null=True, blank=False)
    location = models.TextField(null=True, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

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

    def __str__(self):
        return self.card_number


class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    rating = models.PositiveIntegerField(default=0)
    rating_num = models.PositiveIntegerField(default=0)
    products_sold = models.BigIntegerField(default=0)
    total_revenue = models.BigIntegerField(default=0)
    account_holder_name = models.CharField(max_length=50, null=True, blank=False)
    account_number = models.CharField(max_length=50, null=True, blank=False)
    name_of_bank = models.CharField(max_length=50, null=True, blank=False)


    def __str__(self):
        return self.name