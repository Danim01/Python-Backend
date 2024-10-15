from rest_framework import serializers 
from Productos.models import Productos

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'name', 'precio', 'stock']