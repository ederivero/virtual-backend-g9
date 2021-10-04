from django.urls import path
from .views import (RegistroController,
                    PlatoController,
                    SubirImagenController,
                    PlatosController,
                    VentaController)
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('registro', RegistroController.as_view()),
    path('login', TokenObtainPairView.as_view()),
    path('refresh-session', TokenRefreshView.as_view()),
    path('platos', PlatosController.as_view()),
    path('subir-imagen', SubirImagenController.as_view()),
    path('plato/<int:id>', PlatoController.as_view()),
    path('pedido', VentaController.as_view()),

]
