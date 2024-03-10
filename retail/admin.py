from django.contrib import admin
from .models import Factory, Network, Entrepreneur


def clear_debt(modeladmin, request, queryset):
    for obj in queryset:
        obj.debt = 0
        obj.save()


clear_debt.short_description = 'Очистить задолженность'

fields_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'supplier', 'time_created']


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'debt', 'time_created']
    list_filter = ('city',)
    actions = [clear_debt]


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = fields_display
    list_filter = ('city',)
    actions = [clear_debt]


@admin.register(Entrepreneur)
class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = fields_display
    list_filter = ('city',)
    actions = [clear_debt]
