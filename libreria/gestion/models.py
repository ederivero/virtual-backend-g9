from django.db import models


# https://docs.djangoproject.com/en/3.2/ref/models/
# https://docs.djangoproject.com/en/3.2/topics/db/models/
class ProductoModel(models.Model):

    class OpcionesUM(models.TextChoices):
        UNIDAD = 'UN', 'UNIDAD'
        DOCENA = 'DOC', 'DOCENA'
        CIENTO = 'CI', 'CIENTO'
        MILLAR = 'MI', 'MILLAR'

    # Tipos de datos del ORM => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-types
    # Parametros genericos de los tipos de datos => https://docs.djangoproject.com/en/3.2/ref/models/fields/#field-options

    productoId = models.AutoField(
        primary_key=True, null=False, unique=True, db_column='id')

    productoNombre = models.CharField(
        max_length=45, db_column='nombre', null=False)

    productoPrecio = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='precio')

    productoUnidadMedida = models.TextField(
        choices=OpcionesUM.choices, default=OpcionesUM.UNIDAD, db_column='unidad_medida')

    def __str__(self):
        return self.productoNombre

    class Meta:
        """Link de la documentacion https://docs.djangoproject.com/en/3.2/ref/models/options/"""
        # db_table => indica el nombre de la tabla en la bd
        db_table = 'productos'
        # ordering => modifica el ordenamiento por defecto (x el id) al momento de devolver los registros
        # si queremos que sea ASC se pondra solamente el nombre del atributo, si queremos que sea DESC antes del atributo pondremos un guion (-)
        ordering = ['-productoPrecio']
        # verbose_name y verbonse_name_plural => sirven para el panel administrativo (CMS) de django
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class ClienteModel(models.Model):
    # NOTA: si vamos a usar el panel administrativo de Django entonces solo ahi se debe usar el verbose_name y el help_text
    clienteId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    clienteNombre = models.CharField(
        max_length=45, db_column='nombre', verbose_name='nombre', help_text='Ingresa aqui el nombre')

    clienteDocumento = models.CharField(
        max_length=12, db_column='documento', unique=True, verbose_name='documento del cliente')

    clienteDireccion = models.CharField(
        max_length=100, db_column='direccion', verbose_name='direccion')

    def __str__(self):
        # Metodo que permite sobreescribir la forma en la cual se mostrara el objeto por consola al ser consultado en su totalidad
        return self.clienteNombre

    class Meta:
        db_table = 'clientes'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'


class CabeceraModel(models.Model):
    # tipos = VENTA V | COMPRA C
    class OpcionesTipo(models.TextChoices):
        VENTA = 'V', 'VENTA'
        COMPRA = 'C', 'COMPRA'

    cabeceraId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    cabeceraFecha = models.DateTimeField(auto_now_add=True, db_column='fecha')

    cabeceraTipo = models.TextField(
        choices=OpcionesTipo.choices, db_column='tipo', null=False)

    # related_name => sirve para ingresar desde la clase ClienteModel a todos sus registros de cabeceras
    # on_delete => que accion debe tomar cuando un registro de esa FK es eliminado, sus valores pueden ser:
    # CASCADE => elimina ese cliente y luego todas sus cabeceras
    # PROTECT => no permite la eliminacion de los clientes siempre y cuando tengan una cabecera
    # SET_NULL => elimina el cliente y todas sus cabeceras la cambia el valor a null
    # DO_NOTHING => no hace nada, mantiene su valor a pesar que se elimino dicho cliente
    # RESTRICT => restringe la eliminacion
    # https://docs.djangoproject.com/en/3.2/topics/db/examples/
    clientes = models.ForeignKey(to=ClienteModel, db_column='clientes_id',
                                 null=False, related_name='clienteCabeceras', on_delete=models.PROTECT)

    class Meta:
        db_table = 'cabecera_operaciones'
        verbose_name = 'cabecera'
        verbose_name_plural = 'cabeceras'


class DetalleModel(models.Model):
    detalleId = models.AutoField(
        db_column='id', primary_key=True, unique=True, null=False)

    detalleCantidad = models.IntegerField(db_column='cantidad', null=False)

    detalleImporte = models.DecimalField(
        max_digits=5, decimal_places=2, db_column='importe', null=False)

    productos = models.ForeignKey(to=ProductoModel, db_column='productos_id',
                                  on_delete=models.PROTECT, related_name='productoDetalles', null=False)

    cabeceras = models.ForeignKey(to=CabeceraModel, db_column='cabecera_operaciones_id',
                                  on_delete=models.PROTECT, related_name='cabeceraDetalles', null=False)

    class Meta:
        db_table = 'detalle_operaciones'
        verbose_name = 'detalle'
        verbose_name_plural = 'detalles'
