from django.urls import path
from . import views 
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  path('Users/', views.SignUp.as_view()),
  path('Users/<int:pk>/', views.SignUp.as_view()),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]