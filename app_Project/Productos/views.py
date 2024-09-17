from django.http import HttpResponse, JsonResponse
from Productos.models import Productos
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt

def index(request, pk=None):

  if request.method == "GET":
    if pk:
      Products = Productos.objects.get(id = pk)
      return JsonResponse(data = {"Message": "Ok", 
                                  "id": Products.id, 
                                  "name": Products.name, 
                                  "Precio": Products.precio, 
                                  "stock": Products.stock})
    else:
      Products = list(Productos.objects.all().values(
        "id", "name", "precio", "stock"
      ))
    return JsonResponse(data = {"Message": "Ok", "Producto": Products})
  
  if request.method == "POST":

    body = request.body.decode('utf-8')
    request_body = json.loads(body)

    product = Productos.objects.create(
      name = request_body["name"],
      precio = request_body["precio"],
      stock = request_body["stock"]
    )

    return JsonResponse(data = {"Message": "Ok", "name": product.name, "Precio": product.precio, "stock": product.stock})

  if request.method == "DELETE":
    if pk:
      Productos.objects.get(id = pk).delete()
    return JsonResponse(data = {"Message": "se elemino", "pk": pk})
  
  return HttpResponse("Metodo no disponible", status=405)

# Productos.objects.filter(nombre del elemento que quiero eliminar)