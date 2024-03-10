from django.urls import path, include
from rest_framework import routers

from products.apps import ProductsConfig
from products.views import FactoryProductViewSet, NetworkProductViewSet, EntrepreneurProductViewSet

app_name = ProductsConfig.name

router = routers.DefaultRouter()
router.register(r'factory_product', FactoryProductViewSet)
router.register(r'network_product', NetworkProductViewSet)
router.register(r'entrepreneur_product', EntrepreneurProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
