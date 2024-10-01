from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app_users.models import CustomUser
from app_users.serializers import CustomUserSerializer

# Create your views here.
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def CustomUser_request(request, pk=None):
    """
    Retrieve, update or delete a code snippet.
    """
    if pk is not None:  # Solo busca el usuario si pk está presente
        try:
            list_user = CustomUser.objects.get(id=pk)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        list_user = None

    if request.method == 'GET':
        if pk is None:
          Users = CustomUser.objects.all()
          list_users = CustomUserSerializer(Users, many=True)
          return Response(list_users.data)
        else:
          User = CustomUserSerializer(list_user)
          return Response(User.data)

    elif request.method == 'POST':
        User = CustomUserSerializer(data = request.data)
        print(User, request.data)
        if User.is_valid():
            User.save()
            return Response(User.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        User = CustomUserSerializer(list_user, data=request.data)
        if User.is_valid():
            User.save()
            return Response(User.data)
        return Response(User.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        list_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
