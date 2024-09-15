from django.shortcuts import render
from django.http import HttpResponse
from Productos import Productos

# Create your views here.
def index(request):

  if request == "GET":
    products = Productos
    return HttpResponse("Hola, estas accediendo a la vista de productos")