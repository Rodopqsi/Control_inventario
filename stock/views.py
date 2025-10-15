from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ProveedorForm, ProductoForm
from .models import Proveedor, Producto
from django.db.models.deletion import ProtectedError


def home(request):
    return redirect('producto_list')


# Proveedor CRUD
def proveedor_list(request):
    proveedores = Proveedor.objects.all().order_by('nombre')
    return render(request, 'stock/proveedor_list.html', {'proveedores': proveedores})


def proveedor_create(request):
    form = ProveedorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Proveedor creado correctamente.')
        return redirect('proveedor_list')
    return render(request, 'stock/proveedor_form.html', {'form': form})


def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Proveedor actualizado correctamente.')
        return redirect('proveedor_list')
    return render(request, 'stock/proveedor_form.html', {'form': form, 'proveedor': proveedor})


def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        try:
            proveedor.delete()
            messages.success(request, 'Proveedor eliminado.')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar: tiene productos asociados.')
        return redirect('proveedor_list')
    return render(request, 'stock/confirm_delete.html', {'object': proveedor, 'type': 'Proveedor'})


# Producto CRUD
def producto_list(request):
    productos = Producto.objects.select_related('proveedor').all().order_by('nombre')
    return render(request, 'stock/producto_list.html', {'productos': productos})


def producto_create(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Producto creado correctamente.')
        return redirect('producto_list')
    return render(request, 'stock/producto_form.html', {'form': form})


def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Producto actualizado correctamente.')
        return redirect('producto_list')
    return render(request, 'stock/producto_form.html', {'form': form, 'producto': producto})


def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado.')
        return redirect('producto_list')
    return render(request, 'stock/confirm_delete.html', {'object': producto, 'type': 'Producto'})
