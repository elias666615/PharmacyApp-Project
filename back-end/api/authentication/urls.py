from django.urls import path
from .views import CardInfoAPIView, CountriesAPIView, RegisterView, RolesAPIView, VerifyEmail, LoginAPIView
from django.conf.urls import url

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    url('roles/', RolesAPIView.as_view()),
    url('countries/', CountriesAPIView.as_view()),
    url('transfer/', CardInfoAPIView.as_view())
]