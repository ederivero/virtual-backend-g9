from rest_framework.test import APITestCase
from .models import ProductoModel


class ProductosTestCase(APITestCase):

    def setUp(self):
        ProductoModel(productoNombre='Producto 01',
                      productoPrecio=20.40, productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 02',
                      productoPrecio=20.40, productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 03',
                      productoPrecio=20.40, productoUnidadMedida='UN').save()
        ProductoModel(productoNombre='Producto 04',
                      productoPrecio=20.40, productoUnidadMedida='UN').save()

    def test_post_fail(self):
        '''Deberia fallar el test cuando no le pasamos la informacion'''
        # BLOQUE DE DESCRIPCION DEL TEST

        # BLOQUE DE DEFINICION DE VARIABLES
        request = self.client.post('/gestion/productos/')
        message = request.data.get('message')

        # BLOQUE DE TESTEO DE RESULTADOS
        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Error al guardar el producto')

    def test_post_success(self):
        '''Deberia retornar el producto creado'''

        request = self.client.post('/gestion/productos/', data={
            "productoNombre": "Cartulina Canson Blanca",
            "productoPrecio": 1.50,
            "productoUnidadMedida": "UN"
        }, format='json')
        message = request.data.get('message')
        id = request.data.get('content').get('productoId')

        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()

        self.assertEqual(request.status_code, 201)
        self.assertEqual(message, 'Producto creado exitosamente')
        self.assertIsNotNone(productoEncontrado)

    def test_get_success(self):
        '''Deberia retornar los productos almacenados'''
        # yo le pase parametros de paginacion x la url
        # productoEncontrado = ProductoModel.objects.all()
        request = self.client.get(
            '/gestion/productos/', data={'pagina': 1, 'cantidad': 2})

        # pagina = 1 && cantidad = 2
        # testen que en la paginacion se cumpla lo sgte:
        paginacion = request.data.get('paginacion')
        content = request.data.get('data').get('content')

        # paginaPrevia => null
        self.assertIsNone(paginacion.get('paginaPrevia'))
        # paginaContinua != null
        self.assertIsNotNone(paginacion.get('paginaContinua'))
        # porPagina = 2
        self.assertEqual(paginacion.get('porPagina'), 2)
        # data.content => Lista cuya longitud sea 2
        self.assertEqual(len(content), 2)
