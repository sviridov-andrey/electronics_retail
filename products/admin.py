from django.contrib import admin
from products.models import FactoryProduct, NetworkProduct, EntrepreneurProduct


@admin.register(FactoryProduct)
class FactoryProductAdmin(admin.ModelAdmin):
    pass


@admin.register(NetworkProduct)
class NetworkProductAdmin(admin.ModelAdmin):
    pass


@admin.register(EntrepreneurProduct)
class EntrepreneurProductAdmin(admin.ModelAdmin):
    pass
