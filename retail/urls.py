from django.urls import path, include
from rest_framework import routers
from retail.apps import RetailConfig
from retail.views import FactoryViewSet, NetworkViewSet, EntrepreneurViewSet

app_name = RetailConfig.name


router = routers.DefaultRouter()
router.register(r'factory', FactoryViewSet)
router.register(r'network', NetworkViewSet)
router.register(r'entrepreneur', EntrepreneurViewSet)
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
