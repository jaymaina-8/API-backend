from django.contrib import admin
from .models import Product, UserRegistration

# Register your models here.

admin.site.register(Product)
admin.site.register(UserRegistration)