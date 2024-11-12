from django.contrib import admin
from .models import Productos, UserProductos

# Register your models here.
admin.site.register(Productos)
admin.site.register(UserProductos)
