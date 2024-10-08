from django.db import models


# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="user name")
    last_name = models.CharField(max_length=50, null=False, blank=False, verbose_name="user last name")
    age = models.IntegerField(max_length=2, verbose_name="user age")
    address = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=20, default='Colombia')

