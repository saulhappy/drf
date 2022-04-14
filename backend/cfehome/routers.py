from wsgiref.simple_server import demo_app
from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

router = DefaultRouter()

router.register("products-2", ProductViewSet, basename="products")

urlpatterns = router.urls