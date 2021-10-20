from rest_framework_simplejwt.views import TokenObtainPairView
# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomPayloadSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.request import Request
from .permissions import CorreoPermission


class CustomPayloadController(TokenObtainPairView):
    """Sirve para modificar el payload de la token de acceso"""
    permission_classes = [AllowAny]
    serializer_class = CustomPayloadSerializer

    def post(self, request):
        data = self.serializer_class(data=request.data)
        if data.is_valid():
            print(data.validated_data)
            return Response(data={
                "success": True,
                "content": data.validated_data,
                "message": "Login exitoso"
            })

        else:
            return Response(data={
                "success": False,
                "content": data.errors,
                "message": "error de generacion de la jwt"
            })


class PerfilUsuario(RetrieveAPIView):

    permission_classes = [IsAuthenticated, CorreoPermission]

    def get(self, request: Request):
        # me devolver la instancia del usuario y si no hay un AnonymousUser
        print(request.user)
        print(request.auth)  # me devolvera la token y si no hay un None
        return Response(data={
            'message': 'El usuario es',
            'content': request.user.usuarioCorreo
        })
