from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import RegistroSerializer


class RegistroController(CreateAPIView):
    serializer_class = RegistroSerializer

    def post(self, request: Request):
        data = self.serializer_class(data=request.data)

        if data.is_valid():
            return Response(data={
                'message': 'Usuario creado exitosamente'
            })
        else:
            return Response(data={
                'message': 'Error al crear el usuario'
            })
