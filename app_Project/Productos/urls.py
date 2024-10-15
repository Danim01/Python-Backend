from django.urls import path
from Productos import views 

urlpatterns = [
  path('productosAll/', views.ProductoView.as_view(), name="ProductoView"),
  path('producto/<int:pk>', views.ProductoView.as_view(), name="get_one"),
  path('delete/<int:pk>', views.ProductoView.as_view(), name="delete"),
  path('put/<int:pk>', views.ProductoView.as_view(), name="put"),
  path('post/', views.ProductoView.as_view(), name="post")
]