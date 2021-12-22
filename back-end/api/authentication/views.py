from re import A
from django.db import models
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.serializers import Serializer

from .models import Card_Information, Role, Store, User
from .serializers import CardInfoSerializer, RegisterSerializer, RoleSerializer, LoginSerializer, StoreSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        _user = request.data
        serializer = self.serializer_class(data=_user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user=User.objects.get(email=user_data['email'])
        print(_user['city'])
        print(_user['street'])
        print(_user['location'])
        user.city = _user['city']
        user.street = _user['street']
        user.location = _user['location']
        user.save()
        token = RefreshToken.for_user(user).access_token
        print(str(token))
        print(settings.SECRET_KEY)
        try:
            payload = jwt.decode(str(token), settings.SECRET_KEY, algorithms=['HS256'])
            user=User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
            
        # current_site = get_current_site(request).domain
        # relativeLink= reverse('email-verify')
        # absurl = 'http://' + current_site + relativeLink + "?token=" + str(token)
        # email_body='Hi ' + user.first_name + ' ' + user.last_name + '. User link below to verfiy your email \n' + absurl
        # data={'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

        # Util.sendEmail(data)

        if _user['role'] == 'SLR':
            new_store = Store.objects.create(
                owner=user, 
                name=_user['storename'], 
                account_holder_name = _user['account_holder_name'],
                account_number = _user['account_number'],
                name_of_bank = _user['name_of_bank'])
            new_store.save()

        return Response(user_data, status=status.HTTP_201_CREATED)



class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)

class UserAPIView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        email = request.query_params['email']
        user = User.objects.get(email = email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        pass


class RolesAPIView(APIView):
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        roles = Role.objects.all()
        return roles

    def get(self, request):
        roles = self.get_queryset()
        serializer = RoleSerializer(roles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        role_data = request.data
        new_role = Role.objects.create(
            code = role_data['code'],
            description = role_data['description']
        )
        new_role.save()
        serializer = RoleSerializer(new_role)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CardInfoAPIView(APIView):
    serializer_class = CardInfoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        cards = Card_Information.objects.all()
        return cards
    
    def get(self, request):
        user = request.query_params['user']
        try:
            card = Card_Information.objects.get(user__email=user)
        except:
            return Response({'message':'card information not found'}, status=status.HTTP_204_NO_CONTENT)
        serializer = CardInfoSerializer(card)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        card_data = request.data
        user = User.objects.get(email=card_data['user'])
        new_card = Card_Information.objects.create(
            user = user,
            card_number = card_data['card_number'],
            expiry_pate = card_data['expiry_pate'],
            name_on_card = card_data['name_on_card'],
            cvv = card_data['cvv']
        )
        new_card.save()
        return Response({'message': 'card infomation successfully created'}, status=status.HTTP_201_CREATED)


class StoreAPIView(APIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        stores = Store.objects.all()
        return stores

    def get(self, request):
        user_email = request.query_params['user']
        store = Store.objects.get(owner__email = user_email)
        serializer = StoreSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        store = Store.objects.get(id=data['id'])
        if data['update_type'] == 'info':
            pass
        elif data['update_type'] == 'revenue':
            store.products_sold = data['products_sold']
            store.total_revenue = data['total_revenue']
        elif data['update_type'] == 'rating':
            store.rating_num = data['rating_num']
            store.rating = data['rating']
        store.save()
        return Response({'message': 'store successfully updated'}, status=status.HTTP_200_OK)
        