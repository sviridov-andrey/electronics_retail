from django.urls import path, include
from rest_framework import routers
from retail.views import FactoryViewSet, NetworkViewSet, EntrepreneurViewSet, ProductViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name


router = routers.DefaultRouter()
router.register(r'factory', FactoryViewSet)
router.register(r'network', NetworkViewSet)
router.register(r'entrepreneur', EntrepreneurViewSet)
router.register(r'product', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
