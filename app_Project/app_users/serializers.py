from app_users.models import CustomUser
from rest_framework import serializers  

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'age', 'country']