from rest_framework import serializers
from .models import Category, Color, Product, Brand, Cart, Order, CartItem, Images
from rest_framework.serializers import ModelSerializer, ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework import status


class ImageSerializer(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ['id', 'product', 'image_urls', 'image1', 'image2', 'image3', 'image4', 'image5']
    
    def get_image_urls(self, obj):
        # Rasmlar faqat `None` bo'lmagan qiymatlar bilan qaytariladi
        images = [getattr(obj, f'image{i}') for i in range(1, 6)]
        valid_images = [image.url for image in images if image]  # None bo'lmaganlarini olish
        return valid_images

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Faqat `null` bo'lmagan qiymatlarni qaytaradi
        return {key: value for key, value in data.items() if value is not None}
    

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(read_only=True) 

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'category',
            'brand',
            'price',
            'old_price',
            'quantity',
            'description',
            'color',
            'size',
            'created_at',
            'updated_at',
            'images',  
        ]
    

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryRetriveSerializer(ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # related_name='products'
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'cart', 'quantity']


class CartSerializer(serializers.ModelSerializer):  
    cart_items = CartItemSerializer(many=True, read_only=True) 
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'updated_at', 'cart_items', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password_confirmation = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password', 'password_confirmation', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise ValidationError({"password_confirmation": "Parollar mos emas."})

        validate_password(password)
        return data

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        validated_data.pop('password_confirmation') 
        password = validated_data.pop('password')
        
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        user.groups.set(groups_data)
        return user
    

