from django.contrib import admin
from .models import Category, Color, Product, Order, Brand, Cart, CartItem, Images
# Register your models here.
# elbe2008s

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Brand)


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'brand', 'color', 'quantity')
    list_filter = ('category', 'brand', 'color')
    inlines = [ImagesInline]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price')
    list_filter = ('user',)
    inlines = [CartItemInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'cart', 'status')
    list_filter = ('user',)

admin.site.register(CartItem)