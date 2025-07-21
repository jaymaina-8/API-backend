from rest_framework import serializers
from .models import Product, UserRegistration


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = '__all__'