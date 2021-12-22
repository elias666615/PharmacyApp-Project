from rest_framework import fields, serializers
from .models import Card_Information, Role, Store, User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    role=serializers.CharField(max_length=3)
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number', 'role', 'city', 'street', 'location']

    def validate(self, attrs):
        email = attrs.get('email', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        phone_number = attrs.get('phone_number', '')
        role = attrs.get('role', '')
        city = attrs.get('city', '')
        street = attrs.get('street', '')
        location = attrs.get('location', '')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255, min_length=3)
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    Accesstoken=serializers.CharField(max_length=68, min_length=6, read_only=True)
    Refreshtoken=serializers.CharField(max_length=68, min_length=6, read_only=True)
    
    class Meta:
        model=User
        fields=['email', 'password', 'Accesstoken', 'Refreshtoken']

    def validate(self, attrs):
        email=attrs.get('email', '')
        password=attrs.get('password', '')

        print(email)
        print("password: " + password + " *")
        user = auth.authenticate(email=email, password=password)
        print(user)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        print(user.tokens()['access'])

        return {
            'email': user.email,
            'Accesstoken': user.tokens()['access'],
            'Refreshtoken': user.tokens()['refresh'],
        }


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'code', 'description']


class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_Information
        fields = ['id', 'user', 'card_number', 'expiry_pate', 'name_on_card', 'cvv']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'rating', 'products_sold', 'total_revenue', 'account_holder_name', 'account_number', 'name_of_bank']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'first_name', 'last_name', 'role', 'city', 'street', 'location']
        depth = 1