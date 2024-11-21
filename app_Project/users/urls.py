from django.urls import path
from .views import SignUp, Profile 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
  path('signup/', SignUp.as_view()),
  path('login/', TokenObtainPairView.as_view()),
  path('profile/', Profile.as_view()),
  # Debe estar para poder ejecutar la api de los token y refresh
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]