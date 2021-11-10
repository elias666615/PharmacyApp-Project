from django.contrib import admin
from .models import User, Role, Country, Store, Card_Information
# Register your models here.

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Country)
admin.site.register(Store)
admin.site.register(Card_Information)