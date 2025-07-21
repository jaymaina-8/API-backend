from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()


    def __str__(self):
        return self.name

class UserRegistration(models.Model):
    full_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.username