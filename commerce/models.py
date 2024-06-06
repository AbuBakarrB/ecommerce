from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to = "products/images")
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    USER_TYPE_CHOICES = [
        ("buyer", "Buyer"),
        ("seller", "Seller")
        ]
    
    user_type = models.CharField(max_length = 7, choices = USER_TYPE_CHOICES, default="buyer")
    
    @property
    def is_buyer(self):
        return self.user_type == "buyer"
    
    @property
    def is_seller(self):
        return self.user_type == "buyer"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    customer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)