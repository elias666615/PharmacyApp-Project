from django.db import models
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import serializers
from rest_framework.serializers import Serializer

from .models import Card_Information, Country, Role, User
from .serializers import CardInfoSerializer, CountrySerializer, RegisterSerializer, RoleSerializer, LoginSerializer
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
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user=User.objects.get(email=user_data['email'])
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

        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        pass


class RolesAPIView(APIView):
    serializer_class = RoleSerializer

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


class CountriesAPIView(APIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        countries = Country.objects.all()
        return countries

    def get(self, request):
        countries = self.get_queryset()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        country_data = request.data
        new_country = Country.objects.create(
            code = country_data['code'],
            description = country_data['description'],
            phone_code = country_data['phone_code']
        )
        new_country.save()
        serializer = CountrySerializer(new_country)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CardInfoAPIView(APIView):
    serializer_class = CardInfoSerializer

    def get_queryset(self):
        cards = Card_Information.objects.all()
        return cards
    
    def get(self, request):
        cards = self.get_queryset()
        serializer = CardInfoSerializer(cards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        card_data = request.data
        user = User.objects.get(pk=card_data['user'])
        new_card = Card_Information.objects.create(
            user = user,
            card_number = card_data['card_number'],
            expiry_pate = card_data['expiry_pate'],
            name_on_card = card_data['name_on_card'],
            cvv = card_data['cvv']
        )
        new_card.save()
        serializer = CardInfoSerializer(new_card)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
