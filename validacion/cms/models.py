from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authManager import UsuarioManager


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    usuarioId = models.AutoField(
        primary_key=True,
        unique=True,
        db_column='id'
    )

    usuarioNombre = models.CharField(
        max_length=20,
        null=False,
        db_column='nombre',
        verbose_name='Nombre del usuario'
    )

    usuarioApellido = models.CharField(
        max_length=20,
        null=False,
        db_column='apellido',
        verbose_name='Apellido del usuario'
    )

    usuarioCorreo = models.EmailField(
        db_column='correo',
        null=False,
        unique=True,
        verbose_name='Correo del usuario'
    )

    password = models.TextField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    updateAt = models.DateTimeField(
        auto_now=True,
        db_column='updated_at'
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'usuarioCorreo'
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido']

    class Meta:
        db_table = 'usuarios'
