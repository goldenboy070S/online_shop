from rest_framework.serializers import ModelSerializer
from .models import Category, Color, Product, Order, Brand


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    
class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'