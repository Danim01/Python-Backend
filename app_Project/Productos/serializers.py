from rest_framework import serializers 
from productos.models import Productos, UserProductos

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'name', 'precio', 'stock']

class UserProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProductos
        fields = ['id', 'selling_date', 'products_amount', 'client', 'product']
        depth = 1