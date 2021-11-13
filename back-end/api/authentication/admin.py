from django.contrib import admin
from .models import User, Store, Card_Information, Role
# Register your models here.

admin.site.register(User)
admin.site.register(Card_Information)
admin.site.register(Store)
admin.site.register(Role)