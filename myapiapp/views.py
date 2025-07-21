from rest_framework import viewsets
from .models import Product, UserRegistration
from .serializer import ProductSerializer, UserRegisterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegisterSerializer