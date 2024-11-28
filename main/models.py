from typing import Any
from django.db import models
from django.contrib.auth.models import User
from jsonschema import ValidationError
from model_utils.models import TimeStampedModel
from model_utils import FieldTracker
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.__dict__['name']
    




class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.__dict__['name']
    

class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.__dict__['name']


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    size = models.CharField(max_length=50, help_text="misol uchun", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Images(models.Model):
    image1 = models.ImageField(upload_to="products")
    image2 = models.ImageField(upload_to="products", null=True, blank=True)
    image3 = models.ImageField(upload_to="products", null=True, blank=True)
    image4 = models.ImageField(upload_to="products", null=True, blank=True)
    image5 = models.ImageField(upload_to="products", null=True, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='images')

    @property
    def image_urls(self):
        return tuple(
            getattr(self, f"image{i}").url if getattr(self, f"image{i}") else None
            for i in range(1, 6)
        )


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

    @property
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.cart_items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.product.name} for {self.cart.user.username}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Completed', 'Completed')])
    tracker = FieldTracker(fields=['status'])

    # def save(self, *args, **kwargs):
    #     if self.cart and Order.objects.filter(cart=self.cart).exists():
    #         raise ValidationError("This cart has already been linked to an order.")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.status}"

