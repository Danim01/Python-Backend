from django.urls import path
from . import views 

urlpatterns = [
  path("", views.CustomUser_request, name="CustomUser_request"),
  path('<int:pk>/', views.CustomUser_request, name="CustomUser_request")
]