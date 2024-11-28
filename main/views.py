import json

from rest_framework.decorators import action
from rest_framework import status
from django.http import HttpResponse
from rest_framework.exceptions import NotFound
from django.shortcuts import render
from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.response import Response
from .serializers import ColorSerializer, CategorySerializer, BrandSerializer, OrderSerializer, ProductSerializer, UserSerializer, CartSerializer, CartItemSerializer, ImageSerializer, CategoryRetriveSerializer
from .models import Category, Color, Product, Order, Brand, Cart, CartItem, Images
from rest_framework.viewsets import ModelViewSet, ViewSet
from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = queryset.get(pk=pk)
        serializer = CategoryRetriveSerializer(category)
        return Response(serializer.data)


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
        

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category')
        color = self.request.query_params.get('color')
        brand = self.request.query_params.get('brand')
        if category:
            return Product.objects.filter(category=category)
        elif color:
            return Product.objects.filter(color=color)
        elif brand:
            return Product.objects.filter(brand=brand)
        return Product.objects.all()


class IsAuthenticatedOrPostOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' or request.user.is_superuser:
            return True
        return False


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticatedOrPostOnly]


class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ImageViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class CartItemViewSet(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        cart = serializer.validated_data['cart']
        
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.quantity += serializer.validated_data['quantity']
            cart_item.save()
        else:
            serializer.save()

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        
        if not product_id:
            return Response({'detail': 'Product ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise NotFound('Product not found')

        cart = Cart.objects.get(user=request.user)

        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            cart_item.quantity += int(quantity)
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product=product, quantity=quantity)

        return Response({'detail': 'Item added to cart successfully.'}, status=status.HTTP_201_CREATED)


