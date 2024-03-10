from django.contrib import admin
from products.models import FactoryProduct, NetworkProduct, EntrepreneurProduct


@admin.register(FactoryProduct)
class FactoryProductAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(NetworkProduct)
class NetworkProductAdmin(admin.ModelAdmin):
    list_display = '__all__'


@admin.register(EntrepreneurProduct)
class EntrepreneurProductAdmin(admin.ModelAdmin):
    list_display = '__all__'
