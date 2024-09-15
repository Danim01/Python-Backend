from django.db import models

# Create your models here.
class Productos(models.Model):
  
  # productos_id = models.IntegerField(primary_key=true)
  name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Producto name")
  precio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Producto precio")
  stock = models.IntegerField(verbose_name="Productos stock")