from rest_framework import fields, serializers
from .models import Card_Information, Country, Role, Store, User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    country=serializers.CharField(max_length=2)
    role=serializers.CharField(max_length=3)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name', 'phone_number', 'country', 'role']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        first_name = attrs.get('first_name', '')
        last_name = attrs.get('last_name', '')
        phone_number = attrs.get('phone_number', '')
        country = attrs.get('country', '')
        role = attrs.get('role', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255, min_length=3)
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    username=serializers.CharField(max_length=255, min_length=3, read_only=True)
    tokens=serializers.CharField(max_length=68, min_length=6, read_only=True)
    
    class Meta:
        model=User
        fields=['email', 'password', 'username', 'tokens']

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
        
        return {
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens()
        }


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'code', 'description']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'code', 'description', 'phone_code']


class CardInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card_Information
        fields = ['id', 'user', 'card_number', 'expiry_pate', 'name_on_card', 'cvv']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'owner', 'name', 'location']