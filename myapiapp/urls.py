from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register('products',ProductViewSet)
router.register('register',UserRegistrationViewSet)

urlpatterns = [
    path('',include(router.urls)),

]
