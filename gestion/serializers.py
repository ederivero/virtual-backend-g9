from rest_framework import serializers
from .models import DetalleModel, ProductoModel, ClienteModel, CabeceraModel


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


class DetalleOperacionSerializer(serializers.Serializer):
    cantidad = serializers.IntegerField(required=True, min_value=1)

    importe = serializers.DecimalField(
        max_digits=5, decimal_places=2, min_value=0.01, required=True)

    producto = serializers.IntegerField(required=True, min_value=1)


class OperacionSerializer(serializers.Serializer):
    tipo = serializers.ChoiceField(
        choices=[('V', 'VENTA'), ('C', 'COMPRA')], required=True)

    cliente = serializers.CharField(required=True, min_length=8, max_length=11)

    detalle = DetalleOperacionSerializer(many=True)

    # detalle2= serializers.ListField(child=DetalleOperacionSerializer)


class DetalleOperacionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleModel
        # fields = '__all__'
        exclude = ['cabeceras']
        depth = 1


class OperacionModelSerializer(serializers.ModelSerializer):
    cabeceraDetalles = DetalleOperacionModelSerializer(
        # source='cabeceraDetalles',
        many=True)

    class Meta:
        model = CabeceraModel
        fields = '__all__'
        # con el atributo depth indicare cuantos niveles quiero agregar para mostrar la informacion en el caso de las FK's
        depth = 1
