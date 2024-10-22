from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView
from Productos.serializers import productosSerializer
from Productos.models import Productos
from django.http import Http404

# Create your views here.

class ProductoView(APIView):

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



# @csrf_exempt

# def index(request, pk=None):
#   if request.method == "DELETE":
#     if pk:
#       Productos.objects.get(id = pk).delete()
#     return JsonResponse(data = {"Message": "se eliminó", "pk": pk})
  
#   if request.method == "PATCH":
#     body = request.body.decode('utf-8')
#     request_body = json.loads(body)

#     update_producto = {}

#     if "name" in request_body:
#       update_producto["name"] = request_body["name"]

#     if "precio" in request_body:
#       update_producto["precio"] = request_body["precio"]

#     if "stock" in request_body:
#       update_producto["stock"] = request_body["stock"]

#     filas_afectadas = Productos.objects.filter(id = pk).update(**update_producto)

#     if filas_afectadas == 0:
#       return JsonResponse({"error":"No se pudo hacer los cambios"}, status=404)
    
#     producto_modificado = Productos.objects.get(id = pk)
#     return JsonResponse(data = {"Message": "Ok", 
#                                   "id": producto_modificado.id, 
#                                   "name": producto_modificado.name, 
#                                   "Precio": producto_modificado.precio, 
#                                   "stock": producto_modificado.stock})


  
#   return HttpResponse("Método no disponible", status=405)

# # Productos.objects.filter(nombre del elemento que quiero eliminar)