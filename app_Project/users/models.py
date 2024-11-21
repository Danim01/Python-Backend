from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

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

    # Crea una instancia de la clase manager para crear la relación entre el modelo y la BD
    objects = CustomUserManager()

    def __str__(self):
        return self.email