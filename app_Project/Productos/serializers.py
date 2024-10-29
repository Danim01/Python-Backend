from rest_framework import serializers 
from productos.models import Productos

class productosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'name', 'precio', 'stock']