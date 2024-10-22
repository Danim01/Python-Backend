from django.urls import path
from Productos import views 

urlpatterns = [
  path('productos', views.ProductoView.as_view()),
  path('productos/<int:pk>', views.ProductoView.as_view()),
]