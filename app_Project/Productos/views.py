from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Productos.models import Productos

# Create your views here.
def index(request):

  if request.method == "GET":
    Products = list(Productos.objects.all().values(
      "id", "name", "precio", "stock"
    ))
    return JsonResponse(data = {"Message": "Ok", "Producto": Products})