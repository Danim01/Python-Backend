from django.http import HttpResponse, JsonResponse
from Productos.models import Productos
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader

# Create your views here.
@csrf_exempt

def index(request, pk=None):
  if request.method == "GET":
  #   if pk:
  #     Products = Productos.objects.get(id = pk)
  #     return JsonResponse(data = {"Message": "Ok", 
  #                                 "id": Products.id, 
  #                                 "name": Products.name, 
  #                                 "Precio": Products.precio, 
  #                                 "stock": Products.stock})
  #   else:
  #     Products = list(Productos.objects.all().values(
  #       "id", "name", "precio", "stock"
  #     ))
  #   return JsonResponse(data = {"Message": "Ok", "Producto": Products})
  
  # if request.method == "POST":
  #   body = request.body.decode('utf-8')
  #   request_body = json.loads(body)

  #   product = Productos.objects.create(
  #     name = request_body["name"],
  #     precio = request_body["precio"],
  #     stock = request_body["stock"]
  #   )

  #   return JsonResponse(data = {"Message": "Ok", "name": product.name, "Precio": product.precio, "stock": product.stock})
    products_list = Productos.objects.all()
    template = loader.get_template('productos/index.html')
    message = {"products_list": products_list}
    return HttpResponse(template.render(message, request))

  if request.method == "DELETE":
    if pk:
      Productos.objects.get(id = pk).delete()
    return JsonResponse(data = {"Message": "se eliminó", "pk": pk})
  
  if request.method == "PATCH":
    body = request.body.decode('utf-8')
    request_body = json.loads(body)

    update_producto = {}

    if "name" in request_body:
      update_producto["name"] = request_body["name"]

    if "precio" in request_body:
      update_producto["precio"] = request_body["precio"]

    if "stock" in request_body:
      update_producto["stock"] = request_body["stock"]

    filas_afectadas = Productos.objects.filter(id = pk).update(**update_producto)

    if filas_afectadas == 0:
      return JsonResponse({"error":"No se pudo hacer los cambios"}, status=404)
    
    producto_modificado = Productos.objects.get(id = pk)
    return JsonResponse(data = {"Message": "Ok", 
                                  "id": producto_modificado.id, 
                                  "name": producto_modificado.name, 
                                  "Precio": producto_modificado.precio, 
                                  "stock": producto_modificado.stock})


  
  return HttpResponse("Método no disponible", status=405)

# Productos.objects.filter(nombre del elemento que quiero eliminar)