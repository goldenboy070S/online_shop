from django.contrib import admin
from .models import Category, Color, Product, Order, Brand
# Register your models here.
# elbe2008s

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand', 'color', 'quantity')
    list_filter = ('category', 'brand', 'color')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at', 'quantity', 'get_price')
    list_filter = ('product',)