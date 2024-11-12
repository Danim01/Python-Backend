from django.urls import path
from productos import views 

urlpatterns = [
  path('', views.ProductoView.as_view()),
  path('<int:pk>/', views.ProductoView.as_view()),
  path('<int:user_id>/', views.UserProductsView.as_view()),
  path('<str:date_from>,<str:date_to>/', views.UserProductsDateView.as_view()),
]