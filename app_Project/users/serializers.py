from users.models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'last_name', 'age', 'email', 'password']
        # Hace validaciones extra, en este caso la contraseña solo va a ser
        # serializada en las peticiones POST y PATCH, en las tipo GET no va
        # a aparecer este campo
        extra_kwargs = {'password': {'write_only': True}}
    
    # Esta función solo se ejecuta cuando en la vista utilizo el serializador y le paso
    # datos, primero valida los datos y luego ejecuta la función con los datos validados
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)

        return user

class LogInInputSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(min_length=8)
