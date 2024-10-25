from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    size = models.CharField(max_length=50, help_text="misol uchun", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image1 = models.ImageField(upload_to="products")
    image2 = models.ImageField(upload_to="products", null=True, blank=True)
    image3 = models.ImageField(upload_to="products", null=True, blank=True)
    image4 = models.ImageField(upload_to="products", null=True, blank=True)
    image5 = models.ImageField(upload_to="products", null=True, blank=True)
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_price(self):
        return self.product.price * self.quantity