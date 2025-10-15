from django.contrib import admin

from .models import Proveedor, Producto


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'contacto')
    search_fields = ('nombre', 'contacto')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'stock', 'precio', 'proveedor')
    list_filter = ('proveedor',)
    search_fields = ('nombre',)
