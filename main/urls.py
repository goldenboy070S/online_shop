from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ColorViewSet, BrandViewSet, OrderViewSet, ProductViewSet

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('color', ColorViewSet)
router.register('brand', BrandViewSet)
router.register('order', OrderViewSet)
router.register('product', ProductViewSet)

urlpatterns = router.urls