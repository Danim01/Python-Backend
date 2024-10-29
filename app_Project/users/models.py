from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Eliminar el campo username
    username = None

    # Hacer que el correo sea único
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50, verbose_name="User Name")
    age = models.IntegerField(verbose_name="User Age")

    # Utilizar el correo como el identificador para el login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age']

    # Definir los nombres relacionados al modelo y a sus permisos
    # por unos únicos para evitar conflictos con el modelo user de django
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
    )

    def __str__(self):
        return self.email