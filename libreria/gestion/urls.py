from django.urls import path
from .views import (PruebaController,
                    ProductosController,
                    ProductoController,
                    ClienteController)

urlpatterns = [
    path('prueba/', PruebaController.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view()),
    path('clientes/', ClienteController.as_view()),
]
