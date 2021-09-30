from django.contrib.auth.models import BaseUserManager


# BaseUserManager => sirve para modificar el comportamiento de la creacion de un usuario x consola, nos permite modificar POR COMPLETO al modelo auth
# UserManager => nos permite modificar campos como el firstName y lastName, agregar nuevos campos
class ManejoUsuarios(BaseUserManager):

    def create_user(self, email, nombre, apellido, tipo, password=None):
        """Creacion de un usuario"""
        if not email:
            raise ValueError('El usuario tiene que tener un correo valido')
        # validar mi correo y ademas lo normalizo haciendolo todo en minusculas
        email = self.normalize_email(email)
        # Creo mi instancia del usuario
        usuarioCreado = self.model(usuarioCorreo=email, usuarioNombre=nombre,
                                   usuarioApellido=apellido, usuarioTipo=tipo)

        # set_password() => encriptara la contraseña
        usuarioCreado.set_password(password)
        # sirve para referencia a que bse de datos estoy haciendo la creacion, esto se utilizara mas que todo para cuando tengamos multiples bases de datos en nuestro proyecto
        usuarioCreado.save(using=self._db)

        return usuarioCreado

    def create_superuser(self, email, nombre, apellido, tipo, password):
        '''Creacion de un super usuario (administrador)'''

        nuevoUsuario = self.create_user(
            email, nombre, apellido, tipo, password)

        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)
