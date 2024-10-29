from users.models import CustomUser
from rest_framework import serializers  

class CustomUserSerializer(serializers.ModelSerializer):
    # name = serializers.CharField()
    # last_name = serializers.CharField(source="last_name")
    # age = serializers.CharField()
    # address = serializers.CharField()
    # country = serializers.CharField()
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'last_name', 'age', 'email', 'password']

class OutputSerializer(serializers.Serializer):
    accessToken = serializers.CharField(source='access_token')
    refreshToken = serializers.CharField(source='refresh_token')
    name = serializers.CharField()