from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductoModel
from .serializers import ProductoSerializer
from rest_framework import status
from .utils import PaginacionPersonalizada


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
