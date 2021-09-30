from django.db import models
from .authManager import ManejoUsuarios
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser


class PlatoModel(models.Model):
    platoId = models.AutoField(
        primary_key=True, null=False, db_column='id', unique=True)

    platoNombre = models.CharField(
        max_length=100, db_column='nombre', null=False)

    platoPrecio = models.DecimalField(
        db_column='precio', max_digits=5, decimal_places=2, null=False)

    # sirve para almacenar imagenes en el servidor
    # a diferencia del FileField el imageField solamente permitira el guardado de archivos con extension de imagenes (.jpg, .png, .svg, .jpeg)
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#imagefield
    platoFoto = models.ImageField(
        upload_to='platos/', db_column='foto', null=True)

    platoCantidad = models.IntegerField(
        db_column='cantidad', null=False, default=0)

    # se actualizara su valor cuando el registro sufra alguna modificacion
    # auto_now => agarrara la fecha actual cuando parte del registro o en su totalidad sea modificada
    updatedAt = models.DateTimeField(db_column='updated_at', auto_now=True)

    # auto_now_add => cuando se cree un nuevo registro, agarrara la fecha actual y lo creara en esta columna
    createdAt = models.DateTimeField(db_column='created_at', auto_now_add=True)

    class Meta:
        db_table = 'platos'


class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    # si queremos modificar todo el auth model entonces tendremos que usar el AbstractBaseUser, si quieremos solamente modificar first_name, last_name, entonces usaremos el AbstractUser
    # PermissionsMixin => es la clase encargada de dar todos los permisos a nivel administrativo
    TIPO_USUARIO = [(1, 'ADMINISTRADOR'), (2, 'MOZO'), (3, 'CLIENTE')]

    usuarioId = models.AutoField(
        primary_key=True, db_column='id', unique=True, null=False)

    usuarioNombre = models.CharField(max_length=50, db_column='nombre')

    usuarioApellido = models.CharField(
        max_length=50, db_column='apellido', verbose_name='Apellido del usuario')

    usuarioCorreo = models.EmailField(
        max_length=50, db_column='email', unique=True)

    usuarioTipo = models.IntegerField(choices=TIPO_USUARIO, db_column='tipo')

    password = models.TextField(null=True)

    # configurar los campos base de nuestro modelo auth
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # TODO LO SIGUIENTE ES PARA CUANDO VAYAMOS A INGRESAR UN ADMINISTRADOR POR CONSOLA:

    # ahora agregamos el comportamiento cuando se llame al createsuperuser y al create user
    objects = ManejoUsuarios()

    # definimos la columna que sera la encargada de validar que el usuario sea unico e irrepetible
    USERNAME_FIELD = 'usuarioCorreo'

    # es lo que pedira la consola cuando se llame al createsuperuser
    REQUIRED_FIELDS = ['usuarioNombre', 'usuarioApellido', 'usuarioTipo']

    class Meta:
        db_table = 'usuarios'


class PedidoModel(models.Model):
    pedidoId = models.AutoField(primary_key=True, db_column='id', unique=True)

    pedidoFecha = models.DateTimeField(auto_now_add=True, db_column='fecha')

    pedidoTotal = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='total')

    cliente = models.ForeignKey(
        to=UsuarioModel, related_name='clientePedidos', db_column='cliente_id')

    vendedor = models.ForeignKey(
        to=UsuarioModel, related_name='vendedorPedidos', db_column='vendedor_id')

    class Meta:
        db_table = 'pedidos'


class DetallePedidoModel(models.Model):
    detalleId = models.AutoField(primary_key=True, db_column='id', unique=True)

    detalleCantidad = models.IntegerField(
        db_column='cantidad', null=False, min_value=0)

    detalleSubTotal = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='sub_total')

    plato = models.ForeignKey(
        to=PlatoModel, related_name='platoDetalles', db_column='plato_id')

    pedido = models.ForeignKey(
        to=PedidoModel, related_name='pedidoDetalles', db_column='pedido_id')

    class Meta:
        db_table = 'detalles'
