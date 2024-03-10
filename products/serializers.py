from rest_framework import serializers
from .models import EntrepreneurProduct, NetworkProduct, FactoryProduct


class FactoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryProduct
        fields = '__all__'


class NetworkProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkProduct
        fields = '__all__'


class EntrepreneurProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntrepreneurProduct
        fields = '__all__'
