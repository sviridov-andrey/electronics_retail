from django.urls import path, include
from rest_framework import routers
from users.apps import UsersConfig

app_name = UsersConfig.name


router = routers.DefaultRouter()
# router.register(r'retail', RetailViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
