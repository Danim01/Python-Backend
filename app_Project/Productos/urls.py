from django.urls import path
from productos import views 

urlpatterns = [
  path('', views.ProductoView.as_view()),
  path('<int:pk>/', views.ProductoView.as_view()),
  path('<int:pk>/', views.UserProductsView.as_view()),
]