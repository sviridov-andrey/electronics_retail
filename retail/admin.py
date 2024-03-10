from django.contrib import admin
from .models import Factory, Network, Entrepreneur


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_filter = ('city',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_filter = ('city',)


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = '__all__'
    list_filter = ('city',)
