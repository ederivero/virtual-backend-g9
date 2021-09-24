from django.urls import path
from .views import PruebaController, ProductosController, ProductoController

urlpatterns = [
    path('prueba/', PruebaController.as_view()),
    path('productos/', ProductosController.as_view()),
    path('producto/<int:id>', ProductoController.as_view())
]
