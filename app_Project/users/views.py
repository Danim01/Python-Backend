from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import APIView 
from rest_framework.response import Response 
from users.models import CustomUser
from users.serializers import CustomUserSerializer

class SignUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_salida = {
                "name": serializer.data.name,
                "age": serializer.data.age,
            }
            return Response(data=user_salida.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profile(APIView):
    # Sirve para proteger la ruta de usuarios que no están autenticados y
    # si el usuario esta autenticado en la request me aparece una instancia
    # del usuario 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user, many=False)
        return Response(data = serializer.data, status=status.HTTP_200_OK)

   
    

    
