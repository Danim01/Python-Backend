from django.db import models


# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Producto name")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Producto name")
    age = models.IntegerField(verbose_name="Productos stock")
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=20, default='Colombia')

