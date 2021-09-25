from rest_framework import serializers
from .models import ProductoModel, ClienteModel


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        # esto vinculara el serializador con el modelo respectivo para jalar sus atributos y hacer las validaciones correspondientes
        model = ProductoModel

        # indica que campos tengo q mostrar para la deserealizacion
        # fields = '__all__' => indicara que haremos uso de todas los atributos del modelo
        fields = '__all__'
        # fields = ['productoNombre', 'productoPrecio']

        # exclude = ['campo1', 'campo2'] => excluira tanto de la peticion como del retorno de elementos los atributos indicados
        # exclude = ['productoId']

        # no se puede utilizar los dos atributos al mismo tiempo, es decir, o usamos el exclude o usamos el fields


class ClienteSerializer(serializers.ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/fields/
    clienteNombre = serializers.CharField(
        max_length=45, required=False, trim_whitespace=True, read_only=True)
    clienteDireccion = serializers.CharField(
        max_length=100, required=False, trim_whitespace=True)

    class Meta:
        model = ClienteModel
        fields = '__all__'
