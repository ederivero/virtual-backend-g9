from rest_framework import serializers
from .models import UsuarioModel


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioModel
        fields = '__all__'
