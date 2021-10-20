from rest_framework import permissions
from rest_framework.request import Request


class CorreoPermission(permissions.BasePermission):
    # si queremos modificar el message o el code, entonces no podremos usar comparadores en el atributo permission_classes ya que no lo respetara, en ese caso tendremos que usarlos como una tupla [permiso1, permiso2, ...] y asi ira recorriendo 1x1 esperando a que se cumplan todos los permisos
    message = 'Permiso no concedido.'

    def has_permission(self, request: Request, view):
        print(view)
        print(request)
        if(request.user.usuarioCorreo == 'ederiveroman@gmail.com'):
            return True
        else:
            return False
