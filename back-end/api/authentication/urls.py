from django.urls import path
from .views import CardInfoAPIView, RegisterView, RolesAPIView, VerifyEmail, LoginAPIView, StoreAPIView
from django.conf.urls import url

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('stores/', StoreAPIView.as_view(), name="stores"),
    url('roles/', RolesAPIView.as_view()),
    url('transfer/', CardInfoAPIView.as_view())
]