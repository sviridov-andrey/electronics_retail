from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet
from users.apps import UsersConfig

app_name = UsersConfig.name


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
