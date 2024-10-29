from rest_framework import status 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.decorators import APIView 
from rest_framework.response import Response 
from users.models import CustomUser
from users.serializers import CustomUserSerializer, OutputSerializer

class SignUp(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        User = CustomUserSerializer(data = request.data)
        # print(User, request.data)
        User.is_valid(raise_exception=True)
        
        if CustomUser.objects.filter(email = User.validated_data['email']).exists():
            return Response({"error": "El correo electrónico ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        # El doble ** sirve para desempaquetar datos uno por uno de un diccionario
        user = CustomUser.objects.create(**User.validated_data)

        refresh = RefreshToken.for_user(user)

        user_salida = OutputSerializer({
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),
            "user_id": user.id,
            "name": user.name,
            "age": user.age,
        })

        return Response(data=user_salida.data, status=status.HTTP_201_CREATED )
    
    def get_object(self, pk):
        try:
            list_user = CustomUser.objects.get(id=pk)
            return (list_user)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        if pk == None:
            Users = CustomUser.objects.all()
            list_users = CustomUserSerializer(Users, many=True)
            return Response(list_users.data)
        else:
            Users = self.get_object(pk)
            User = CustomUserSerializer(Users)
            return Response(User.data)
        
# class SignUp(APIView):
#     permission_classes = [AllowAny]

#     def get_object(self, pk):
#         try:
#             list_user = CustomUser.objects.get(id=pk)
#             return (list_user)
#         except CustomUser.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk=None):
#         if pk == None:
#             Users = CustomUser.objects.all()
#             list_users = CustomUserSerializer(Users, many=True)
#             return Response(list_users.data)
#         else:
#             Users = self.get_object(pk)
#             User = CustomUserSerializer(Users)
#             return Response(User.data)

#     def delete(self, request, pk):
#         list_user = self.get_object(pk)
#         list_user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
#     def put(self, request, pk):
#         list_user = self.get_object(pk)
#         User = CustomUserSerializer(list_user, data=request.data)
#         # La función is_valid() sirve para validar los datos de entrada de mi serializers
#         # Si el serializer es válido, se guardan los datos en la base de datos,
#         # si el serializer no es válido, se devuelve los errores y un código de estado HTTP 400 Bad Request
#         if User.is_valid():
#             User.save()
#             return Response(User.data)
#         return Response(User.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
