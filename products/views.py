from rest_framework import viewsets
from products.models import FactoryProduct, NetworkProduct, EntrepreneurProduct
from products.serializers import FactoryProductSerializer, NetworkProductSerializer, EntrepreneurProductSerializer


class FactoryProductViewSet(viewsets.ModelViewSet):
    queryset = FactoryProduct.objects.all()
    serializer_class = FactoryProductSerializer


class NetworkProductViewSet(viewsets.ModelViewSet):
    queryset = NetworkProduct.objects.all()
    serializer_class = NetworkProductSerializer


class EntrepreneurProductViewSet(viewsets.ModelViewSet):
    queryset = EntrepreneurProduct.objects.all()
    serializer_class = EntrepreneurProductSerializer
