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

    def create_superuser(self, usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password):
        '''Creacion de un super usuario (administrador)'''
        # los parametros que va a recibir tienen que ser los mismos que hubiesemos declarado en el usuarioModel REQUIRED_FIELD y en el USERNAME_FIELD , llegaran con esos mismo nombre de parametros y en el caso que se escribiese mal, lanzara un error de argumento inesperado

        nuevoUsuario = self.create_user(
            usuarioCorreo, usuarioNombre, usuarioApellido, usuarioTipo, password)

        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)
