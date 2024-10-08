from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from app_users.models import CustomUser
from app_users.serializers import CustomUserSerializer

# Create your views here.
@api_view(['GET'])
def get_user_request(request, pk):
    try:
        list_user = CustomUser.objects.get(id=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
          User = CustomUserSerializer(list_user)
          return Response(User.data)

@api_view(['GET'])
def get_all_request(request):
    if request.method == 'GET':
        Users = CustomUser.objects.all()
        list_users = CustomUserSerializer(Users, many=True)
        return Response(list_users.data)
    
@api_view(['DELETE'])
def delete_user_request(request, pk):
    try:
        list_user = CustomUser.objects.get(id=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        list_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT'])
def put_user_request(request, pk):
    try:
        list_user = CustomUser.objects.get(id=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        User = CustomUserSerializer(list_user, data=request.data)
        # La función is_valid() sirve para validar los datos de entrada de mi serializers
        # Si el serializer es válido, se guardan los datos en la base de datos,
        # si el serializer no es válido, se devuelve los errores y un código de estado HTTP 400 Bad Request
        if User.is_valid():
            User.save()
            return Response(User.data)
        return Response(User.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_user_request(request):
    if request.method == 'POST':
        User = CustomUserSerializer(data = request.data)
        print(User, request.data)
        if User.is_valid():
            User.save()
            return Response(User.data, status=status.HTTP_201_CREATED)

    
