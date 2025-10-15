from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=150)
    contacto = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self) -> str:  # pragma: no cover
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    stock = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, related_name='productos')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self) -> str:  # pragma: no cover
        return self.nombre
