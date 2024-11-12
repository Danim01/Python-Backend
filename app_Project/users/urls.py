from django.urls import path
from . import views 
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
  path('', views.SignUp.as_view()),
  path('signUp/', views.SignUp.as_view()),
  path('login/', views.Login.as_view()),
  path('profile/', views.Profile.as_view()),
  path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh')
]