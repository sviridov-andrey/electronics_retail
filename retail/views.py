from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Factory, Network, Entrepreneur, Product
from .serializers import FactorySerializer, NetworkSerializer, EntrepreneurSerializer, ProductSerializer


class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('country',)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    

class EntrepreneurViewSet(viewsets.ModelViewSet):
    queryset = Entrepreneur.objects.all()
    serializer_class = EntrepreneurSerializer

