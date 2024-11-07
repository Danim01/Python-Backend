from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView
from productos.serializers import productosSerializer, UserProductosSerializer
from productos.models import Productos
from django.http import Http404
from rest_framework.permissions import AllowAny

# Create your views here.

class ProductoView(APIView):
  permission_classes = [AllowAny]

  def get_object(self, pk):
    try:
      producto = Productos.objects.get(id=pk)
      return producto
    except Productos.DoesNotExist:
      raise Http404

  
  def get(self, request, pk=None):
    if pk == None:
      productos = Productos.objects.all()
      all_productos = productosSerializer(productos, many=True)
      return Response(all_productos.data, status=status.HTTP_200_OK)
    else:
      producto = self.get_object(pk)
      object_producto = productosSerializer(producto)
      return Response(object_producto.data, status=status.HTTP_200_OK)

  def delete(self, request, pk, format=None):
    producto = self.get_object(pk)
    print(producto)
    producto.delete()
    return Response(status=status.HTTP_200_OK)

  def put(self, request, pk):
    producto = self.get_object(pk)
    actualizar = productosSerializer(producto, data=request.data)

    if actualizar.is_valid():
      actualizar.save()
      return Response(actualizar.data)
    return Response(actualizar.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def post(self, request):
    nuevo_producto = productosSerializer(data=request.data)

    if nuevo_producto.is_valid():
      nuevo_producto.save()
      return Response(nuevo_producto.data, status=status.HTTP_200_OK)
    return Response(nuevo_producto.errors, status=status.HTTP_400_BAD_REQUEST)    


class UserProductsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
      serializer = UserProductos.object.get(id=pk)
      productos = UserProductosSerializer(serializer)
      return Response(data=productos.data, status=status.HTTP_200_OK)

      pass

      
    def post(self, request):
        serialized = UsersProductSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        # if UsersProducts.objects.filter(username=serialized.validated_data['product']).exists():
        #     return Response("Purchase already exists.", status=status.HTTP_400_BAD_REQUEST)

        users_products = UsersProducts.objects.create(**serialized.validated_data)

        return Response({"message": "Successfully transaction"}, status=status.HTTP_201_CREATED)
