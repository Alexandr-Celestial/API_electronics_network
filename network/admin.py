from django.contrib import admin

from network.models import NetworkLink, Product


@admin.action(description="Очистить задолженность")
def clean_arrears(modeladmin, request, queryset):
    """Очищает задолженность перед поставщиком у выбранных объектов"""
    queryset.update(arrears=0)


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    """Фильтрует по названию города"""
    list_display = ("name", "email", "city", "arrears", "hierarchy_level")
    list_filter = ("city",)
    actions = [clean_arrears]
    readonly_fields = ("level", "created_at")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Выводит информацию по поставщику"""
    list_display = ("name", "model", "release_date", "supplier")
    list_filter = ("release_date",)
