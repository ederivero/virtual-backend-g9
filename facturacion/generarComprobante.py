from datetime import datetime
from .models import ComprobanteModel
from cms.models import PedidoModel
from django.db import connection


def crearComprobante(tipo_de_comprobante: int, pedido: PedidoModel, documento_cliente: str):
    operacion = 'generar_comprobante'
    if tipo_de_comprobante == 1:
        serie = 'FFF1'  # *
    elif tipo_de_comprobante == 2:
        serie = 'BBB1'
    # SELECT numero FROM comprobantes WHERE serie = '...' ORDER BY numero DESC LIMIT 1;
    # usando RAW queries en el ORM
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT numero FROM comprobantes WHERE serie = '%s' ORDER BY numero DESC LIMIT 1;", (serie))
    ultimoComprobante = ComprobanteModel.objects.values_list('comprobanteNumero').filter(
        comprobanteSerie=serie).order_by('-comprobanteNumero').first()

    if not ultimoComprobante:
        numero = 1
    else:
        numero = ultimoComprobante.comprobanteNumero + 1
    sunat_transaction = 1  # *

    cliente_tipo_de_documento = (
        1 if len(documento_cliente) == 8 else 6) if documento_cliente else 6

    cliente_numero_de_documento = documento_cliente

    cliente_denominacion = pedido.cliente.usuarioNombre + \
        ' '+pedido.cliente.usuarioApellido
    cliente_direccion = ''
    cliente_email = pedido.cliente.usuarioCorreo
    fecha_de_emision = datetime.now()
    moneda = 1
    porcentaje_de_igv = 18
    total = pedido.pedidoTotal
    # una vez generado el comprobante con el tipo de formato no se puede cambiar
    formato_de_pdf = 'TICKET'


def visualizarComprobante():
    pass


# * => depende del contador de la empresa
