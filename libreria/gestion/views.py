from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductoModel, ClienteModel
from .serializers import ProductoSerializer, ClienteSerializer
from rest_framework import status
from .utils import PaginacionPersonalizada
from rest_framework.serializers import Serializer
import requests as solicitudes
from os import environ


class PruebaController(APIView):
    def get(self, request, format=None):
        return Response(data={'message': 'Exito'}, status=200)

    def post(self, request: Request, format=None):
        print(request.data)
        return Response(data={'message': 'Hiciste post'})


class ProductosController(ListCreateAPIView):
    # pondremos la consulta de ese modelo en la bd
    queryset = ProductoModel.objects.all()  # SELECT * FROM productos;
    serializer_class = ProductoSerializer
    pagination_class = PaginacionPersonalizada

    # def get(self, request):
    #     respuesta = self.get_queryset().filter(productoEstado=True).all()
    #     print(respuesta)
    #     # instance => para cuando ya tenemos informacion en la bd y la queremos serializar para mostrarsela al cliente
    #     # data => para ver si la informacion que me esta enviando el cliente esta buena o no
    #     # many => sirve para indicar que estamos pasando una lista de instancias de la clase del modelo
    #     respuesta_serializada = self.serializer_class(
    #         instance=respuesta, many=True)
    #     # el atributo data de la clase ListSerializer sirve para obtener la informacion proveida por el serializador en forma de un diccionario o una lista (en el caso que sean mas de una instancia)
    #     return Response(data={
    #         "message": None,
    #         "content": respuesta_serializada.data
    #     })

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        # raise_exception => lanzara la excepcion con el mensaje que dio el error y no permitira continuar con codigo siguiente
        if data.is_valid():
            # para hacer el guardado de un nuevo registro en la bd es OBLIGATORIO hacer primero el is_valid()
            data.save()

            return Response(data={
                "message": "Producto creado exitosamente",
                "content": data.data
            }, status=status.HTTP_201_CREATED)
        else:
            # data.errors => almacena todos los errores que no han permitido que esa informacion sea valida (is_valid() = false)
            return Response(data={
                "message": "Error al guardar el producto",
                "content": data.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class ProductoController(APIView):

    def get(self, request, id):
        # SELECT * FROM productos WHERE id = id
        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()
        try:
            productoEncontrado2 = ProductoModel.objects.get(productoId=id)
            print(productoEncontrado2)
        except ProductoModel.DoesNotExist:
            print('No se encontro')

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializador = ProductoSerializer(instance=productoEncontrado)
        return Response(data={
            "message": None,
            "content": serializador.data
        })

    def put(self, request: Request, id):
        # 1. busco si el producto existe
        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no existe",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        # 2. modificare los valores proveidos
        serializador = ProductoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.update(instance=productoEncontrado,
                                validated_data=serializador.validated_data)
            # 3. guardare y devolver el producto actualizado
            return Response(data={
                "message": "Producto actualizado exitosamente",
                "content": serializador.data
            })
        else:
            return Response(data={
                "message": "Error al actualizar el producto",
                "content": serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        productoEncontrado: ProductoModel = ProductoModel.objects.filter(
            productoId=id).first()

        if productoEncontrado is None:
            return Response(data={
                "message": "Producto no encontrado",
                "content": None
            }, status=status.HTTP_404_NOT_FOUND)

        # modificar su estado a False
        productoEncontrado.productoEstado = False
        productoEncontrado.save()

        serializador = ProductoSerializer(instance=productoEncontrado)

        return Response(data={
            "message": "Producto eliminado exitosamente",
            "content": serializador.data
        })


class ClienteController(CreateAPIView):
    queryset = ClienteModel.objects.all()
    serializer_class = ClienteSerializer

    def post(self, request: Request):

        data: Serializer = self.get_serializer(data=request.data)
        if data.is_valid():
            # .validated_data => es la data ya validada y se crea a raiz de la llamada al metodo is_valid()
            # .data => es la data sin validacion
            # .initial_data => data inicial tal y como me la esta pasando el cliente
            # print(data.validated_data)
            # print(data.initial_data)
            # print(data.data)
            documento = data.validated_data.get('clienteDocumento')
            direccion = data.validated_data.get('clienteDireccion')

            url = 'https://apiperu.dev/api/'
            if len(documento) == 8:
                # si es DNI validar que en el body venga el clienteDireccion
                if direccion is None:
                    return Response(data={
                        'message': 'Los clientes con DNI se debe proveer la direccion'
                    }, status=status.HTTP_400_BAD_REQUEST)
                url += 'dni/'

            elif len(documento) == 11:
                url += 'ruc/'

            resultado = solicitudes.get(url+documento, headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer '+environ.get('APIPERU_TOKEN')
            })
            # print(resultado.json())
            success = resultado.json().get('success')

            # validar si el dni existe o no
            if success is False:
                return Response(data={
                    'message': 'Documento incorrecto'
                }, status=status.HTTP_400_BAD_REQUEST)

            data = resultado.json().get('data')
            nombre = data.get('nombre_completo') if data.get(
                'nombre_completo') else data.get('nombre_o_razon_social')
            # hacer algo similar con la direccion
            # si la direccion no es vacia (tiene contenido ) su valor seguira siendo la direccion, caso contrario extraeremos la direccion del resultado de APIPERU
            direccion = direccion if direccion else data.get(
                'direccion_completa')

            # guardado del cliente en la bd
            nuevoCliente = ClienteModel(
                clienteNombre=nombre, clienteDocumento=documento, clienteDireccion=direccion)

            nuevoCliente.save()

            nuevoClienteSerializado: Serializer = self.serializer_class(
                instance=nuevoCliente)

            return Response(data={
                'message': 'Cliente agregado exitosamente',
                'content': nuevoClienteSerializado.data
            })
        else:
            return Response(data={
                'message': 'Error al ingresar el cliente',
                'content': data.errors
            })


class BuscadorClienteController(RetrieveAPIView):
    serializer_class = ClienteSerializer

    def get(self, request: Request):
        print(request.query_params)
        # primero validar si me esta pasando el nombre o el documento
        # nombre = '...'
        documento = request.query_params.get('documento')

        # si tengo documento hare una busqueda todos los clientes por ese documento
        if documento:
            clienteEncontrado = ClienteModel.objects.filter(
                clienteDocumento=documento).first()
            # si no existe el cliente retornar un resultado
            if clienteEncontrado is None:
                return Response({
                    'message': 'Cliente no existe'
                }, status=status.HTTP_404_NOT_FOUND)

            data = self.serializer_class(instance=clienteEncontrado)

            return Response({'content': data.data})

        return Response({'message': None})
