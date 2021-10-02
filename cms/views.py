from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImagenSerializer, RegistroSerializer, PlatoSerializer
from .models import PlatoModel
from os import remove
from django.db.models import ImageField
from django.conf import settings


class RegistroController(CreateAPIView):
    serializer_class = RegistroSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)

        if data.is_valid():
            data.save()
            return Response(data={
                'message': 'Usuario creado exitosamente',
                'content': data.data
            })
        else:
            return Response(data={
                'message': 'Error al crear el usuario',
                'content': data.errors
            })


class PlatosController(ListCreateAPIView):
    serializer_class = PlatoSerializer
    queryset = PlatoModel.objects.all()

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data={
                'content': data.data,
                'message': 'Plato creado exitosamente'
            })
        else:
            return Response(data={
                'message': 'Error al crear el plato',
                'content': data.errors
            }, status=400)

    def get(self, request):
        data = self.serializer_class(instance=self.get_queryset(), many=True)
        return Response(data={
            'message': None,
            'content': data.data
        })


class SubirImagenController(CreateAPIView):
    serializer_class = ImagenSerializer

    def post(self, request: Request):
        print(request.FILES)
        data = self.serializer_class(data=request.FILES)

        if data.is_valid():
            archivo = data.save()
            url = request.META.get('HTTP_HOST')

            return Response(data={
                'message': 'Archivo subido exitosamente',
                'content': url + archivo
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el archivo',
                'content': data.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class PlatoController(RetrieveUpdateDestroyAPIView):
    serializer_class = PlatoSerializer
    queryset = PlatoModel.objects.all()

    def patch(self, request, id):
        # actualizacion parcial
        pass

    def put(self, request, id):
        # hacer el put actualizacion total
        pass

    def get(self, request, id):
        platoEncontrado = self.get_queryset().filter(platoId=id).first()

        if not platoEncontrado:
            return Response(data={
                'message': 'Plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        data = self.serializer_class(instance=platoEncontrado)

        return Response(data={
            'content': data.data
        })

    def delete(self, request, id):

        platoEncontrado = self.get_queryset().filter(platoId=id).first()
        if not platoEncontrado:
            return Response(data={
                'message': 'Plato no encontrado'
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            data = platoEncontrado.delete()
            remove(settings.MEDIA_ROOT / str(platoEncontrado.platoFoto))
        except Exception as e:
            print(e)

        # data = PlatoModel.objects.filter(platoId=id).delete()
        # (num_registros_eliminados, { platoModel: id })
        print(data)
        return Response(data={
            'message': 'Plato eliminado exitosamente'
        })
