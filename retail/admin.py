from django.contrib import admin
from .models import Factory, Network, Product, Entrepreneur


class ProductInline(admin.TabularInline):
    model = Product


class FactoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class NetworkAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class EntrepreneurAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


admin.site.register(Factory, FactoryAdmin)
admin.site.register(Network, NetworkAdmin)
admin.site.register(Entrepreneur, EntrepreneurAdmin)
admin.site.register(Product)
