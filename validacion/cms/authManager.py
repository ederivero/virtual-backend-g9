from django.contrib.auth.models import BaseUserManager


class UsuarioManager(BaseUserManager):

    def create_user(self, email, nombre, apellido, password=None):
        if not email:
            raise ValueError(
                "El usuario debe tener obligatoriamente un correo")

        email = self.normalize_email(email)

        nuevoUsuario = self.model(usuarioCorreo=email,
                                  usuarioNombre=nombre, usuarioApellido=apellido)

        nuevoUsuario.set_password(password)

        nuevoUsuario.save(using=self._db)
        return nuevoUsuario

    def create_superuser(self, usuarioCorreo, usuarioNombre, usuarioApellido, password):
        usuario = self.create_user(
            usuarioCorreo, usuarioNombre, usuarioApellido, password
        )
        usuario.is_superuser = True
        usuario.is_staff = True
        usuario.save(using=self._db)
