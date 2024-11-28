from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import CategoryViewSet, ColorViewSet, BrandViewSet, OrderViewSet, ProductViewSet, UserViewSet, CartViewSet, CartItemViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet, basename='product')
router.register(r'images', ImageViewSet)
router.register(r'users', UserViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cartItems', CartItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls