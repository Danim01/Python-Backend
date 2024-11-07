from django.db import models

from users.models import CustomUser

# Create your models here.
class Productos(models.Model):
  
  # productos_id = models.IntegerField(primary_key=true)
  name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Producto name")
  precio = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Producto precio")
  stock = models.IntegerField(verbose_name="Productos stock")

class UserProductos(models.Model):
  selling_date = models.DateField(verbose_name="Selling Date")
  products_amount = models.IntegerField(verbose_name="Products Amount")
  client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Client")
  product = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name="Product")
